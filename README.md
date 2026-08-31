# AI-UE-Asset-Inspector

A learning project exploring **AI + UE5 Technical Art** workflows.

## V0.2 — Add LLM

Current pipeline:

```text
UE5 Asset Folder
      ↓
Python Scanner
      ↓
Structured JSON
      ↓
LLM API
      ↓
AI Asset Report
```

### What I built

* Scan a UE5 asset folder with Python
* Organize scanned files into categories
* Save the result as JSON
* Send the JSON to an LLM
* Generate a Technical Artist-style asset analysis report

### Example

The scanner can identify assets such as:

```text
Instances
Materials
Textures
Tree Assets
```

The LLM then analyzes the asset structure and suggests possible problems.

### What I learned

* `os.walk()`
* Python dictionaries
* JSON
* `.env` and API keys
* `.gitignore`
* LLM API calls
* Passing structured data to an LLM

### Current limitation

The scanner currently mainly knows **file names and paths**.

It cannot yet directly inspect the internal data of `.uasset` files, so some AI analysis may be assumptions rather than confirmed problems.

### Next

**V0.3 — Deeper UE5 asset inspection**
