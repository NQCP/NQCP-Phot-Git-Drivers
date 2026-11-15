# Optics documents (passive optics, no driver)

Datasheets, manuals and test reports for passive optical parts that have no driver of their own:
waveplates, beamsplitters, polarizers, filters, lenses, mirrors, fibre components (the user,
2026-11-15: "Prepare a folder where I can upload docs related to optics in driver").

- **File names**: `<Manufacturer> <Part number> <Document type>.pdf`, e.g.
  `Thorlabs BS039 Datasheet.pdf`, as in the other `photonicdrivers/<Driver>/docs/` folders.
- **A Markdown copy of each PDF** with the same name (`.md`, converted with markitdown) goes beside
  it so it can be searched and read as text. Keep the original PDF unchanged (the user, 2026-11-12;
  see the repo README).
- **Optics in a motorised mount** (e.g. the half-wave plate in an Elliptec ELL14 mount): the
  optic's documents go here; the mount's own manual stays with its driver in
  `photonicdrivers/RotationMounts/docs/`.
- **Measured calibration data** (e.g. a cube's R and T curves) stays in the Analysis repo,
  `analysis/Equipment_Characterization/`. Which part sits where on a station goes into that
  station's `station_facts.md` (Protocols repo).
