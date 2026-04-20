```
____  ____   __   _  _  __    ____  ____  __    __  __ _  ____ 
(  _ \(  _ \ / _\ / )( \(  )  (  __)(  _ \(  )  (  )(  ( \(  __)
 ) _ ( )   //    \\ /\ // (_/\ ) _)  )   // (_/\ )( /    / ) _) 
(____/(__\_)\_/\_/(_/\_)\____/(____)(__\_)\____/(__)\_)__)(____)
```

### THIS TOOL IS FANMADE AND IS NOT IN ANY WAY AFFILIATED WITH SUPERCELL AND ITS SUBSIDIARIES.

# BrawlerLine CLI

A command-line search engine for filtering and identifying Brawl Stars brawlers using structured attributes.

---

## Overview

**BrawlerLine** allows you to query a dataset of brawlers using:

- category filters (rarity, class, attack type, etc.)
- binary flags (dot, cc, dash, etc.)
- fuzzy name matching
- tag-based search

It is designed for fast narrowing of candidates — ideal for “Guess the Brawler”-style gameplay.

---

## Usage

Run the CLI:

```bash
python brawlerline.py
```

You will see:

```
BrawlerLine CLI Started. Type 'exit' to quit or 'help' for flags.
```

---

## Command Syntax

```
[name] [flags]
```

Example:

```
colt -range long --dash 0
```

---

## Name Search

You can type part (or all) of a brawler’s name:

```
co
```

Matches:

- Colt
- Colette
- Cordelius

---

## Category Flags


| Flag           | Description          | Example                   |
| -------------- | -------------------- | ------------------------- |
| `-rarity`      | Filter by rarity     | `-rarity Epic`            |
| `-class`       | Filter by class      | `-class Tank`             |
| `-attack_type` | Type of attack       | `-attack_type projectile` |
| `-pattern`     | Projectile pattern   | `-pattern cone`           |
| `-range`       | Attack range         | `-range long`             |
| `-mobility`    | Movement type        | `-mobility dash`          |
| `-spawns`      | Spawn type           | `-spawns turret`          |
| `-super`       | Super ability type   | `-super knockback`        |
| `-tag`         | Tag-based filtering  | `-tag shotgun`            |
| `-advanced`    | Show developer table | `-advanced`               |


---

## Binary Flags (0 = No, 1 = Yes)


| Flag       | Meaning          |
| ---------- | ---------------- |
| `--dot`    | Damage over time |
| `--cc`     | Crowd control    |
| `--heal`   | Can heal         |
| `--dash`   | Can dash         |
| `--jump`   | Can jump         |
| `--turret` | Has turret       |
| `--pet`    | Has pet          |


Example:

```
--cc 1 --dash 0
```

---

## Output Modes

### Standard Mode

```
NAME            | RARITY       | CLASS        | RANGE      | SUPER
------------------------------------------------------------------
Colt            | Rare         | Damage Dealer| long       | damage
```

---

### Advanced Mode (`-advanced`)

```
NAME            | DOT | CC | HEAL | DASH | JUMP | TURR | PET | MOBILITY
-----------------------------------------------------------------------
Colt            |  F  | F  |  F   |  F   |  F   |  F   |  F  | none
```

---

## Supported Tags

Tags describe unique mechanics or traits. Examples include:

- `shotgun`
- `high_close_damage`
- `wall_break`
- `high_precision`
- `piercing`
- `splash`
- `thrower`
- `trap`

...

Probably shouldn't use these for guessing unless you're REALLY desperate.

---

## 💡 Example Queries

### Find all long-range brawlers:

```
-range long
```

### Find all non-tanks with dash:

```
-class !Tank --dash 1
```

### Find throwers:

```
-attack_type thrower
```

### Find brawlers with pets:

```
--pet 1
```

### Combine filters:

```
-class Damage Dealer -range medium --cc 1
```

---

## Exit Commands

```
exit
quit
```

---

## Notes

- All filters are **case-insensitive**
- Unknown flags are ignored with a warning
- Multiple filters narrow results (AND logic)
- Tags are matched by inclusion

