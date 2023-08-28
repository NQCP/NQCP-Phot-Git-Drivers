def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import photonicdrivers

    photonicdrivers_path = Path(photonicdrivers.__file__).parent
    return versioningit.get_version(project_dir=photonicdrivers_path.parent)


__version__ = _get_version()
