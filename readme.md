# Rampsim-cli
Command line tool to simulate ramps from various healers in WoW.

Main usage is get the time is takes to complete the ramp.

# Usage
1. Type in your spell sequence in the `index.py` file.
2. Type in your haste sheet value (not the percentage) in the `config.toml` file.

## Example sequence
```python
SEQUENCE = [
    yulon,
    enveloping_mist,
    enveloping_mist,
    enveloping_mist,
    enveloping_mist,
    enveloping_mist,
    soothing_mist,
    vivify,
    vivify,
    vivify,
    vivify,
]
```

## Example config file
```toml
[statistics]
haste = 1000
```

# Specializations supported
Currently supported specilizations include:
- Discipline priest
- Mistweaver monk

# Warning
The tool currently does not account for spell cooldowns.

The tool currently does not account for stat diminishing returns.