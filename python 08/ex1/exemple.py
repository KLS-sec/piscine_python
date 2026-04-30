from __future__ import annotations

import sys
import os
import importlib
from typing import Any


def safe_import(module_name: str) -> Any | None:
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def get_version(pkg: str) -> str:
    try:
        from importlib.metadata import version
        return version(pkg)
    except Exception:
        return "unknown"


def check_dependencies() -> dict[str, Any]:
    deps = {
        "numpy": safe_import("numpy"),
        "pandas": safe_import("pandas"),
        "matplotlib": safe_import("matplotlib"),
    }

    # optional dependency
    deps["requests"] = safe_import("requests")

    return deps


def print_dependency_status(deps: dict[str, Any]) -> bool:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    required = ["numpy", "pandas", "matplotlib"]
    ok = True

    for name in required:
        if deps[name] is None:
            print(f"[ERROR] {name} not installed")
            print(f"Install with: pip install {name} OR poetry add {name}")
            ok = False
        else:
            print(f"[OK] {name} ({get_version(name)}) - ready")

    if deps["requests"] is not None:
        print(f"[OK] requests ({get_version('requests')}) - optional API"
               " access ready")

    return ok


def generate_data(np: Any) -> Any:
    return np.random.normal(size=1000)


def process_data(pd: Any, data: Any) -> Any:
    df = pd.DataFrame(data, columns=["values"])
    df["normalized"] = (df["values"] - df["values"].mean()) / df["values"].std()
    return df


def visualize_data(plt: Any, df: Any) -> None:
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Distribution")
    plt.savefig("matrix_analysis.png")


def show_environment_info() -> None:
    print("\nEnvironment info:")
    print(f"Python executable: {sys.executable}")
    print(f"Virtual env: {os.environ.get('VIRTUAL_ENV', 'None')}")


def show_package_manager_note() -> None:
    print("\nPackage management comparison:")
    print("- pip: installs from requirements.txt into environment")
    print("- poetry: manages env + dependencies via pyproject.toml")


def main() -> None:
    deps = check_dependencies()

    show_environment_info()
    show_package_manager_note()

    if not (deps["numpy"] and deps["pandas"] and deps["matplotlib"]):
        print("\nMissing dependencies. Aborting analysis.")
        return

    np = deps["numpy"]
    pd = deps["pandas"]
    plt = deps["matplotlib"].pyplot

    print("\nAnalyzing Matrix data...")
    data = generate_data(np)

    print("Processing 1000 data points...")
    df = process_data(pd, data)

    print("Generating visualization...")
    visualize_data(plt, df)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
