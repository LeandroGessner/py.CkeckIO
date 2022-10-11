def sort_by_ext(files: list[str]) -> list[str]:
    return sorted(files, key=sort_key)


def sort_key(file: str) -> tuple[str, str]:
    name, dot, ext = file.rpartition(".")
        
    return (ext, name) if name else ("", ext) # the code her => (("", ext), (ext, name))[bool(name)] <= has the same result as the code in result statement


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
