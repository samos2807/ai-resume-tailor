# AGENT 4 — Excel Manager

## Role
Update the job tracker after every CV is successfully generated.
You run LAST in the pipeline.

---

## Input
- Company name
- Job title
- Job ID (if available)
- Job URL (if available)
- Folder path where CV was saved
- Date generated
- Any special notes (e.g. "Attach grade sheet", "GPA below requirement")

---

## Tracker location
C:\Users\samos\OneDrive\שולחן העבודה\Job-Search\Job_Applications_Tracker.xlsx

---

## What to do

Open the tracker and add a new row with:

| Column | Value |
|--------|-------|
| # | Next number in sequence |
| Company | Company name |
| Job Title | Job title |
| Job ID | Job ID if provided, else empty |
| Date Added | Today's date (DD/MM/YYYY) |
| CV Created | Today's date (DD/MM/YYYY) |
| CV Sent | Empty |
| Contact Person | Empty |
| Follow-up (3 days) | Empty |
| Status | CV Ready |
| Job Link | =HYPERLINK("[job_url]","Open Job") if URL provided, else empty |
| CV Folder | =HYPERLINK("[folder_path]","Open Folder") |
| Notes | Any relevant notes |

---

## Status color coding
Apply yellow background (FFF2CC) to Status cell when value is "CV Ready"

---

## Output
```
✅ Tracker updated.
Row added: [Company] — [Job Title] — CV Ready
```

---

## Error handling
If tracker file not found:
```
⚠️ Tracker not found at expected path.
Please check: C:\Users\samos\OneDrive\שולחן העבודה\Job-Search\Job_Applications_Tracker.xlsx
```
