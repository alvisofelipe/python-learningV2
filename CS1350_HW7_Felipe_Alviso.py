import json
import pickle
import os
import shutil


# =====================================================================
# Problem 1: Security Log Splitter and Status Report
# =====================================================================

def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        machines: dict mapping machine name -> log file name
    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}
    with open("info.log", "w") as info_f, \
         open("warning.log", "w") as warning_f, \
         open("error.log", "w") as error_f:
        outputs = {"INFO": info_f, "WARNING": warning_f, "ERROR": error_f}

        for machine, log_name in machines.items():
            counts[machine] = {"INFO": 0, "WARNING": 0, "ERROR": 0}
            with open(log_name, "r") as log_f:
                for line in log_f:
                    line = line.strip()
                    if line == "":          # ignore blank lines
                        continue
                    for level, out_f in outputs.items():
                        if "[" + level + "]" in line:
                            out_f.write(machine + " | " + line + "\n")
                            counts[machine][level] += 1
                            break
    return counts


def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)

    totals = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for machine, c in counts.items():
        total = c["INFO"] + c["WARNING"] + c["ERROR"]
        if c["ERROR"] >= 2:
            status = "CRITICAL"
        elif c["ERROR"] >= 1 or c["WARNING"] >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"
        print(f"{machine}: {total} entries | INFO {c['INFO']} | "
              f"WARNING {c['WARNING']} | ERROR {c['ERROR']} | Status: {status}")
        for level in totals:
            totals[level] += c[level]

    print("-" * 40)
    grand_total = sum(totals.values())
    print(f"Total: {grand_total} entries | INFO {totals['INFO']} | "
          f"WARNING {totals['WARNING']} | ERROR {totals['ERROR']}")

    print(f"Errors (see {error_file}):")
    with open(error_file, "r") as f:
        for line in f:
            print("  " + line.rstrip("\n"))


# =====================================================================
# Problem 2: Incident Tracker
# =====================================================================

def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []
    with open(csv_file, "r") as f:
        next(f, None)                       # skip header line
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            incidents.append({
                "id": int(parts[0]),
                "machine": parts[1],
                "severity": parts[2],
                "description": parts[3],
            })
    return incidents


def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": [],
    }
    for inc in incidents:
        m = inc["machine"]
        s = inc["severity"]
        summary["by_machine"][m] = summary["by_machine"].get(m, 0) + 1
        summary["by_severity"][s] = summary["by_severity"].get(s, 0) + 1
        if s == "high":
            summary["high_ids"].append(inc["id"])

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "incidents.pkl"), "wb") as f:
        pickle.dump(incidents, f)

    by_machine = {}
    for inc in incidents:
        by_machine.setdefault(inc["machine"], []).append(inc)

    for machine, items in by_machine.items():
        with open(os.path.join(folder, machine + ".json"), "w") as f:
            json.dump(items, f)

    return sorted(os.listdir(folder))


def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as f:
        return pickle.load(f)


# =====================================================================
# Problem 3 (Bonus): Workspace Organizer and Backup System
# =====================================================================

def organize(folder):
    """Move files into logs/, data/, pickles/, other/ by extension."""
    categories = {".log": "logs", ".csv": "data", ".json": "data",
                  ".pkl": "pickles"}
    moved = {"logs": [], "data": [], "pickles": [], "other": []}

    for name in sorted(os.listdir(folder)):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):        # leave subfolders alone
            continue
        ext = os.path.splitext(name)[1]
        category = categories.get(ext, "other")
        dest_dir = os.path.join(folder, category)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(path, os.path.join(dest_dir, name))
        moved[category].append(name)

    for category in moved:
        moved[category].sort()
    return moved


def create_backup(source_dir, backup_root, label):
    """Copy source_dir to backup_root/backup_<label>; return the new path."""
    os.makedirs(backup_root, exist_ok=True)
    dest = os.path.join(backup_root, "backup_" + label)
    shutil.copytree(source_dir, dest)
    return dest


def verify_backup(source_dir, backup_dir):
    """Return True if every file under source_dir is in backup_dir with the same size."""
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for name in filenames:
            src_path = os.path.join(dirpath, name)
            rel = os.path.relpath(src_path, source_dir)
            bak_path = os.path.join(backup_dir, rel)
            if not os.path.isfile(bak_path):
                return False
            if os.path.getsize(bak_path) != os.path.getsize(src_path):
                return False
    return True


def cleanup_old_backups(backup_root, keep):
    """Delete all but the newest `keep` backups; return sorted names deleted."""
    names = sorted(n for n in os.listdir(backup_root)
                   if os.path.isdir(os.path.join(backup_root, n)))
    num_to_delete = max(len(names) - keep, 0)
    deleted = names[:num_to_delete]          # oldest come first
    for name in deleted:
        shutil.rmtree(os.path.join(backup_root, name))
    return sorted(deleted)


# =====================================================================
# Test code
# =====================================================================

if __name__ == "__main__":
    print("===== Problem 1 =====")
    with open("server_a.log", "w") as f:
        f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
        f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
        f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
        f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
        f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
        f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

    with open("server_b.log", "w") as f:
        f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
        f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
        f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
        f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
        f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
        f.write("\n")
        f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

    counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
    print(counts)
    with open("warning.log", "r") as f:
        print(f.read())
    print_report(counts)

    print("\n===== Problem 2 =====")
    with open("incidents.csv", "w") as f:
        f.write("id,machine,severity,description\n")
        f.write("1,server_a,high,Account root locked\n")
        f.write("2,server_b,high,Disk encryption failed\n")
        f.write("3,server_b,low,Unencrypted volume mounted\n")
        f.write("4,server_a,medium,Repeated failed logins\n")
        f.write("5,server_b,high,Unauthorized access on port 22\n")

    incidents = load_incidents("incidents.csv")
    print(len(incidents))
    print(incidents[0])

    summary = save_summary(incidents, "summary.json")
    print(summary)
    with open("summary.json", "r") as f:
        print(json.load(f) == summary)

    print(archive(incidents, "archive"))
    with open(os.path.join("archive", "server_a.json"), "r") as f:
        print([item["id"] for item in json.load(f)])
    restored = load_archive("archive")
    print(restored == incidents)

    print("\n===== Problem 3 (Bonus) =====")
    # Start clean so the test can be re-run
    for old in ["workspace", "backups"]:
        if os.path.exists(old):
            shutil.rmtree(old)
    os.mkdir("workspace")
    for name in ["a.log", "b.log", "incidents.csv", "summary.json",
                 "incidents.pkl", "notes.txt"]:
        with open(os.path.join("workspace", name), "w") as f:
            f.write(f"Test file: {name}\n")

    print(organize("workspace"))
    print(sorted(os.listdir("workspace")))

    for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
        path = create_backup("workspace", "backups", label)
        print(os.path.basename(path), verify_backup("workspace", path))

    # Damage one backup: verification must now fail
    os.remove(os.path.join("backups", "backup_2026-10-03", "logs", "a.log"))
    print(verify_backup("workspace", os.path.join("backups", "backup_2026-10-03")))

    print(cleanup_old_backups("backups", 2))
    print(sorted(os.listdir("backups")))