import json, argparse, shlex

def create_parser():
    parser = argparse.ArgumentParser(prog="search", add_help=False)
    parser.add_argument("name", nargs="?", default="")
    parser.add_argument("-rarity")
    parser.add_argument("-class", dest="b_class")
    parser.add_argument("-attack_type")
    parser.add_argument("-pattern", dest="projectile_pattern")
    parser.add_argument("-range")
    parser.add_argument("-mobility")
    parser.add_argument("-spawns")
    parser.add_argument("-super", dest="super_type")
    parser.add_argument("-tag")
    
    # New Advanced toggle
    parser.add_argument("-advanced", action="store_true", help="Print full dev table")

    parser.add_argument("--dot", type=int, choices=[0, 1])
    parser.add_argument("--cc", type=int, choices=[0, 1])
    parser.add_argument("--heal", type=int, choices=[0, 1])
    parser.add_argument("--dash", type=int, choices=[0, 1])
    parser.add_argument("--jump", type=int, choices=[0, 1])
    parser.add_argument("--turret", type=int, choices=[0, 1])
    parser.add_argument("--pet", type=int, choices=[0, 1])
    return parser

def main():
    try:
        with open('brawlers.json', 'r') as f:
            brawlers = json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return

    parser = create_parser()
    print('''
____  ____   __   _  _  __    ____  ____  __    __  __ _  ____ 
(  _ \(  _ \ / _\ / )( \(  )  (  __)(  _ \(  )  (  )(  ( \(  __)
 ) _ ( )   //    \\ /\ // (_/\ ) _)  )   // (_/\ )( /    / ) _) 
(____/(__\_)\_/\_/(_/\_)\____/(____)(__\_)\____/(__)\_)__)(____)
    ''')
    print("BrawlerLine CLI Started. Type 'exit' to quit or 'help' for flags.")

    while True:
        try:
            user_input = input("\nBrawlerLine > ").strip()
            if not user_input: continue
            if user_input.lower() in ['exit', 'quit']: break
            
            if user_input.lower() == 'help':
                print("\n[ CATEGORY FLAGS ]\n  -rarity, -class, -attack_type, -pattern, -range, -mobility, -spawns, -super, -tag, -advanced")
                print("\n[ BINARY FLAGS (0=No, 1=Yes) ]\n  --dot, --cc, --heal, --dash, --jump, --turret, --pet")
                continue

            cmd_args = shlex.split(user_input)
            args, unknown = parser.parse_known_args(cmd_args)
            if unknown: print(f"Warning: Unknown flags ignored: {unknown}")

            results = []
            for name, d in brawlers.items():
                if args.name.lower() not in name.lower(): continue
                if args.rarity and d['rarity'].lower() != args.rarity.lower(): continue
                if args.b_class and d['class'].lower() != args.b_class.lower(): continue
                if args.attack_type and d['attack_type'].lower() != args.attack_type.lower(): continue
                if args.projectile_pattern and d['projectile_pattern'].lower() != args.projectile_pattern.lower(): continue
                if args.range and d['range'].lower() != args.range.lower(): continue
                if args.mobility and d['mobility'].lower() != args.mobility.lower(): continue
                if args.spawns and d['spawns'].lower() != args.spawns.lower(): continue
                if args.super_type and d['super_type'].lower() != args.super_type.lower(): continue
                if args.tag and args.tag.lower() not in [t.lower() for t in d.get('tags', [])]: continue

                if args.dot is not None and d['has_dot'] != bool(args.dot): continue
                if args.cc is not None and d['has_cc'] != bool(args.cc): continue
                if args.heal is not None and d['heals'] != bool(args.heal): continue
                if args.dash is not None and d['can_dash'] != bool(args.dash): continue
                if args.jump is not None and d['can_jump'] != bool(args.jump): continue
                if args.turret is not None and d['has_turret'] != bool(args.turret): continue
                if args.pet is not None and d['has_pet'] != bool(args.pet): continue

                results.append((name, d))

            if not results:
                print("No matches found.")
            else:
                if args.advanced:
                    # FULL DEV TABLE
                    head = f"{'NAME':<15} | DOT | CC | HEAL | DASH | JUMP | TURR | PET | MOBILITY"
                    print("\n" + head)
                    print("-" * len(head))
                    for name, d in results:
                        f = lambda x: "T" if x else "F"
                        print(f"{name:<15} |  {f(d['has_dot'])}  | {f(d['has_cc'])}  |  {f(d['heals'])}   |  {f(d['can_dash'])}   |  {f(d['can_jump'])}   |  {f(d['has_turret'])}   |  {f(d['has_pet'])}  | {d['mobility']}")
                else:
                    # STANDARD TABLE
                    header = f"{'NAME':<15} | {'RARITY':<12} | {'CLASS':<12} | {'RANGE':<10} | {'SUPER'}"
                    print("\n" + header)
                    print("-" * len(header))
                    for name, d in results:
                        print(f"{name:<15} | {d['rarity']:<12} | {d['class']:<12} | {d['range']:<10} | {d['super_type']}")
                
                print("-" * 15)
                print(f"Total Matches: {len(results)}")

        except SystemExit: continue
        except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    main()
