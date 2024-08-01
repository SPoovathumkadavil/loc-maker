import sys
import loc


def main():
    l = loc.Loc()
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            print("Usage: loc-maker [-n a=b...] [-a a=b] [-h]")
            print("Options:")
            print("-n, --new: Create a new loc file. Format: a=b c=d ...")
            print("-a, --add: Add a new key-value pair to the loc file. Format: a=b")
            print("-r, --remove: Remove a key-value pair from the loc file. Format: a")
            return
        if sys.argv[i] == "-n" or sys.argv[i] == "--new":
            for j in range(i + 1, len(sys.argv)):
                if "=" in sys.argv[j]:
                    a, b = sys.argv[j].split("=")
                    l.set(a, b)
                else:
                    break
            if l.empty():
                print("No key-value pairs found.")
                return
            if l.write() is False:
                print("Ensure all keys are present. Required keys: " + str(l.get_required()))
                return
            print("New loc file created.")
            return
        if sys.argv[i] == "-a" or sys.argv[i] == "--add":
            l.read()
            if "=" in sys.argv[i + 1]:
                a, b = sys.argv[i + 1].split("=")
                if l.valid(a) is False:
                    print("Key already exists.")
                    return
                l.set(a, b)
                l.write()
                print("Directory added to loc file.")
            else:
                print("Invalid format. Use a=b.")
            return
        if sys.argv[i] == "-r" or sys.argv[i] == "--remove":
            l.read()
            if l.get(sys.argv[i + 1]) is not None:
                l.paths.pop(sys.argv[i + 1])
                if l.write() is False:
                    print("Cannot remove key " + sys.argv[i + 1] + ".")
                    return
                print("Directory removed from loc file.")
            else:
                print("Directory not found.")
            return
    print("No arguments provided. Use -h for help.")


if __name__ == "__main__":
    main()
