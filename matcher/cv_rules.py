"""CV generation rules — v4. Matches reference template exactly.

Read projects from GitHub before generating:
- RISC-V: https://github.com/samos2807/riscv-pipeline
- Fatigue: https://github.com/samos2807/Driver-Drowsiness-FPGA
"""

# ══════════════════════════════════════════════════════════════════════
# 1. DESIGN CONSTANTS — from reference template
# ══════════════════════════════════════════════════════════════════════

NAVY_BLUE = (0x1A, 0x3A, 0x5C)
BLACK = (0x00, 0x00, 0x00)
GRAY_TEXT = (0x55, 0x55, 0x55)
LINK_GREEN = (0x2B, 0x57, 0x97)  # #2B5797 from reference
SEPARATOR_GRAY = "999999"

FONT = "Calibri"
NAME_PT = 22          # Name: biggest, bold, centered, navy
TITLE_PT = 18         # Job title: one size smaller, bold, centered, navy
CONTACT_PT = 11       # Contact: one line, centered
HEADER_PT = 11.5      # Section headers: bold, navy, left-aligned
BODY_PT = 11          # Body text
CHECKMARK_PT = 12     # Checkmark on project bullets
BULLET_PT = 10        # Military bullet text

MARGIN_CM = {"top": 1.0, "bottom": 0.8, "left": 1.27, "right": 1.27}
LINE_SPACING_PT = 12

# ══════════════════════════════════════════════════════════════════════
# 2. CONTACT INFO
# ══════════════════════════════════════════════════════════════════════

PHONE = "054-5449594"
EMAIL = "samos2807@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/amos-sarusi-727827275/"
LINKEDIN_TEXT = "LinkedIn"
GITHUB_URL = "https://github.com/samos2807"
GITHUB_TEXT = "GitHub"

# ══════════════════════════════════════════════════════════════════════
# 3. SKILLS POOL — only include what matches the job
# ══════════════════════════════════════════════════════════════════════

SKILL_POOL = {
    "cadence_tools": {
        "label": "Cadence Tools",
        "content": "Virtuoso, Genus, Innovus, Spectre, Quantus PEX, PVS DRC/LVS",
        "triggers": ["cadence", "virtuoso", "genus", "innovus", "spectre", "quantus", "pvs"],
    },
    "digital_rtl": {
        "label": "Digital / RTL",
        "content": "Verilog, VHDL, RTL design, pipeline architecture, hazard detection, forwarding logic",
        "triggers": ["rtl", "verilog", "vhdl", "digital design", "logic design", "hazard", "pipeline", "processor"],
    },
    "asic_flow": {
        "label": "ASIC Flow",
        "content": "RTL2GDS, synthesis, P&R, signoff STA, DRC/LVS/PEX, timing analysis",
        "triggers": ["asic", "rtl2gds", "rtl-to-gds", "synthesis", "tape-out", "gds", "timing", "signoff", "sta"],
    },
    "fpga": {
        "label": "FPGA",
        "content": "Xilinx Vivado, Kria KR260 SoC-FPGA, Vitis AI, IP integration, DPU deployment",
        "triggers": ["fpga", "vivado", "xilinx", "kria", "vitis", "soc-fpga", "dpu"],
    },
    "physical_analog": {
        "label": "Physical / Analog",
        "content": "Cadence Virtuoso 45nm, transistor-level design, layout, DRC/LVS/PEX, corner and Monte Carlo analysis",
        "triggers": ["physical design", "layout", "floorplan", "analog", "drc", "lvs", "pex", "mixed signal", "corner"],
    },
    "verification": {
        "label": "Verification",
        "content": "Functional simulation, test environment development, corner-case coverage, gate-level validation",
        "triggers": ["verification", "validation", "simulation", "test", "dft", "coverage"],
    },
    "embedded": {
        "label": "Embedded & HW/SW",
        "content": "Embedded C, UART, GPIO, SPI, custom IP blocks, firmware, board-level bring-up, HW/SW integration",
        "triggers": ["embedded", "firmware", "uart", "gpio", "spi", "bring-up", "hw/sw"],
    },
    "scripting": {
        "label": "Scripting",
        "content": "Python, Tcl, EDA automation",
        "triggers": ["python", "tcl", "scripting", "automation"],
    },
}

# ══════════════════════════════════════════════════════════════════════
# 4. PROJECTS — full data from GitHub repos + lab report
# ══════════════════════════════════════════════════════════════════════

PROJECTS = {
    "riscv": {
        "title": "RISC-V 5-Stage Pipelined Processor",
        "meta": "Verilog, Cadence Genus, Innovus | 45nm",
        "github": "https://github.com/samos2807/riscv-pipeline",
        "best_for": ["verification", "rtl", "asic", "processor", "digital design", "synthesis", "dft", "application engineer"],
        "bullets_by_type": {
            "verification": [
                "Implemented {bold}RTL{/bold} in {bold}Verilog{/bold} across 11 modules, built 3 {bold}verification testbenches{/bold} covering 6 {bold}corner-case scenarios{/bold} to ensure logic correctness through systematic {bold}functional verification{/bold}.",
                "Identified forwarding logic bottleneck causing data hazards; applied {bold}root-cause analysis{/bold} and restructured datapath, eliminating all failing test vectors — {bold}debugging{/bold} at microarchitecture level.",
                "Drove full {bold}RTL2GDS flow{/bold} using {bold}Cadence{/bold} Genus and Innovus, achieving 102.3 MHz with WNS +222ps and zero violations — clean {bold}signoff{/bold}, tape-out ready.",
                "Automated synthesis flow with 3 Tcl scripts, enabling reproducible {bold}regression{/bold} runs across design iterations.",
            ],
            "asic_rtl": [
                "Designed 5-stage pipelined {bold}microarchitecture{/bold} in {bold}Verilog{/bold}: IF/ID/EX/MEM/WB with EX-EX and MEM-EX {bold}data forwarding{/bold}, load-use hazard detection with stall/bubble insertion, and branch flush.",
                "Drove full {bold}RTL2GDS flow{/bold} using {bold}Cadence{/bold} Genus for {bold}synthesis{/bold} and Innovus for {bold}P&R{/bold}, achieving 102.3 MHz with WNS +222ps, 7,519 cells — clean {bold}timing closure{/bold}, tape-out ready.",
                "Identified forwarding logic bottleneck; restructured Verilog RTL, improving WNS by 50ps and converging to target frequency — demonstrating {bold}root-cause analysis{/bold} and {bold}PPA optimization{/bold}.",
                "Automated synthesis and P&R flows with 3 Tcl scripts and Python, enabling reproducible {bold}EDA Automation{/bold} across design iterations.",
            ],
            "physical_design": [
                "Drove full {bold}RTL2GDS flow{/bold} using {bold}Cadence Genus{/bold} for {bold}synthesis{/bold} and {bold}Innovus{/bold} for {bold}floorplanning{/bold}, {bold}place-and-route{/bold}, and {bold}timing analysis{/bold} — 102.3 MHz, 7,519 cells, 33,064 um2, zero {bold}DRC{/bold} violations.",
                "Resolved {bold}timing closure{/bold} challenge in forwarding datapath; restructured RTL and re-ran {bold}STA{/bold}, improving WNS by 50ps to achieve clean {bold}signoff{/bold} — tape-out ready.",
                "Automated {bold}synthesis{/bold} and {bold}P&R{/bold} flows with 3 Tcl scripts, enabling reproducible {bold}EDA Automation{/bold} and {bold}data-driven{/bold} {bold}PPA optimization{/bold}.",
                "Implemented RTL in Verilog across 11 modules with 3 testbenches covering 6 scenarios, verifying logic correctness before {bold}physical implementation{/bold}.",
            ],
            "default": [
                "Implemented {bold}RTL{/bold} in {bold}Verilog{/bold} across 11 modules with 3 testbenches covering 6 corner-case scenarios, ensuring logic correctness through systematic {bold}functional verification{/bold}.",
                "Drove full {bold}RTL2GDS flow{/bold} using {bold}Cadence{/bold} Genus for synthesis and Innovus for {bold}place-and-route{/bold}, achieving 102.3 MHz with WNS +222ps, 7,519 cells, and zero {bold}DRC{/bold} violations — clean {bold}signoff{/bold}, tape-out ready.",
                "Identified forwarding logic bottleneck in pipeline datapath; restructured Verilog RTL, improving WNS by 50ps and converging to target frequency — demonstrating {bold}root-cause analysis{/bold} and {bold}timing closure{/bold} skills.",
                "Automated synthesis and P&R flows with 3 Tcl scripts and Python, enabling reproducible {bold}EDA Automation{/bold} and {bold}data-driven{/bold} {bold}PPA optimization{/bold}.",
            ],
        },
        "bullets_full": None,
        "bullet_compressed": "Drove full {bold}RTL2GDS flow{/bold} using {bold}Cadence{/bold} Genus/Innovus (45nm), achieving 102.3 MHz, 7,519 cells, zero violations — tape-out ready.",
    },
    "fatigue": {
        "title": "Driver Fatigue Detection System",
        "meta": "Xilinx Kria KR260 SoC-FPGA, Python",
        "github": "https://github.com/samos2807/Driver-Drowsiness-FPGA",
        "best_for": ["fpga", "embedded", "soc", "system integration", "hw/sw", "deep learning", "vitis", "python"],
        "bullets_full": [
            "Quantized MobileNetV2 from FP32 to INT8 using {bold}Vitis AI{/bold}, achieving 73% model size reduction with only 0.06% accuracy loss — efficient edge deployment on resource-constrained {bold}FPGA{/bold}.",
            "Built complete real-time detection application on {bold}Xilinx Kria KR260{/bold}: DPU inference at ~5ms, multi-modal sensor fusion, and 10-frame temporal filtering, achieving stable {bold}10-12 FPS{/bold} at 640x480 under 15W.",
            "Resolved critical {bold}HW/SW integration{/bold} bug during {bold}board bring-up{/bold} — wrong preprocessing normalization caused 100% false positives; identified root cause and fixed, restoring 99.86% accuracy.",
        ],
        "bullet_compressed": "Built complete real-time detection system on {bold}Xilinx Kria KR260{/bold} SoC-FPGA using {bold}Vitis AI{/bold}, performing {bold}board bring-up{/bold} and {bold}HW/SW integration{/bold} at stable {bold}10-12 FPS{/bold}.",
    },
    "vlsi_lab": {
        "title": "VLSI Analog Lab, Full Design Flow",
        "meta": "Cadence Virtuoso, Spectre, 45nm",
        "best_for": ["analog", "physical design", "layout", "mixed signal", "virtuoso", "corner", "monte carlo", "drc", "lvs", "pex", "application engineer"],
        "bullets_full": [
            "Designed and laid out 6 circuit blocks in {bold}Cadence Virtuoso{/bold} (45nm): CMOS inverter, NAND2, Latch, DFF, Ring Oscillator, and Op-Amp — all passing {bold}DRC/LVS/PEX{/bold} signoff.",
            "Validated Ring Oscillator stability across 5 PVT corners and 100 Monte Carlo runs, achieving 97% yield — production-ready design margins across -40C to 120C.",
            "Resolved Op-Amp slew rate limitation using transistor finger splitting technique, achieving ~7.5 MHz bandwidth — demonstrating {bold}root-cause analysis{/bold} at transistor level.",
            "Characterized DFF timing parameters (T_setup, T_hold, T_cq) through parametric simulation, identifying setup violation boundary — relevant to {bold}timing closure{/bold} and back-end flows.",
        ],
        "bullet_compressed": "Designed and verified multiple circuit blocks in {bold}Cadence{/bold} Virtuoso 45nm with full {bold}DRC/LVS/PEX{/bold} and corner/Monte Carlo analysis.",
    },
    "microblaze": {
        "title": "MicroBlaze Embedded System",
        "meta": "Xilinx Vivado, Embedded C",
        "best_for": ["embedded", "firmware", "hw/sw", "microcontroller"],
        "bullets_full": [
            "Built an embedded system on {bold}MicroBlaze soft-processor{/bold}, integrating {bold}UART, GPIO{/bold}, and {bold}custom IP blocks{/bold} within the Vivado design environment.",
            "Developed {bold}firmware{/bold} in {bold}Embedded C{/bold} for real-time hardware control, performing {bold}HW/SW bring-up{/bold} and end-to-end system validation.",
        ],
        "bullet_compressed": "Built embedded system on {bold}MicroBlaze{/bold} with UART, GPIO, custom IP, performing {bold}HW/SW bring-up{/bold} and firmware development.",
    },
}

# ══════════════════════════════════════════════════════════════════════
# 5. EDUCATION
# ══════════════════════════════════════════════════════════════════════

EDUCATION = {
    "degree": "B.Sc. Electrical Engineering",
    "university": "Ariel University",
    "years": "2021-2025",
    "gpa": "GPA: 84",
}

COURSEWORK_MAP = {
    "verification": "Relevant coursework: VLSI Design, Digital Systems, Computer Architecture, Semiconductor Physics",
    "asic_rtl": "Relevant coursework: VLSI Design, Computer Architecture, Digital Systems, Semiconductor Physics",
    "fpga_embedded": "Relevant coursework: Digital Systems, Computer Architecture, VLSI Design",
    "physical_design": "Relevant coursework: VLSI Design, Semiconductor Physics, Digital Systems",
    "analog": "Relevant coursework: VLSI Design, Semiconductor Physics, Analog Circuits",
    "embedded": "Relevant coursework: Digital Systems, Computer Architecture, Microprocessors",
    "application": "Relevant coursework: VLSI Design, Digital Systems, Computer Architecture, Semiconductor Physics",
    "general": "Relevant coursework: VLSI Design, Computer Architecture, Digital Systems, Semiconductor Physics",
}

# ══════════════════════════════════════════════════════════════════════
# 6. MILITARY — 2 short bullets with soft skills from job
# ══════════════════════════════════════════════════════════════════════

MILITARY = {
    "title_bold": "Tank Commander & Deputy Company Sergeant Major",
    "title_regular": ",  IDF Armored Corps, 2018-2020",
}

MILITARY_BULLET1 = {
    "innovative": "Led a tank crew under high-pressure conditions, demonstrating {bold}leadership{/bold}, {bold}self-discipline{/bold}, and {bold}systematic thinking{/bold} in mission-critical decisions.",
    "independent": "Led a tank crew under high-pressure conditions, demonstrating {bold}self-discipline{/bold}, {bold}independent{/bold} judgment, and {bold}systematic thinking{/bold} in mission-critical decisions.",
    "fast_paced": "Led a tank crew under high-pressure conditions, demonstrating {bold}leadership{/bold}, {bold}self-discipline{/bold}, and {bold}fast-paced{/bold} decision-making in mission-critical operations.",
    "collaborative": "Led a tank crew under high-pressure conditions, demonstrating {bold}leadership{/bold}, {bold}self-discipline{/bold}, and {bold}collaborative{/bold} thinking in mission-critical decisions.",
    "debugging": "Led a tank crew under high-pressure conditions, demonstrating {bold}self-discipline{/bold}, {bold}analytical{/bold} thinking, and systematic decision-making in mission-critical operations.",
    "default": "Led a tank crew under high-pressure conditions, demonstrating leadership, self-discipline, and systematic thinking in mission-critical decisions.",
}

MILITARY_BULLET2 = {
    "innovative": "Managed complex interfaces between diverse units, streamlining workflows and resolving challenges with {bold}precision{/bold} under tight deadlines.",
    "independent": "Managed complex interfaces between diverse units, resolving logistical challenges {bold}independently{/bold} with high {bold}precision{/bold} under tight deadlines.",
    "fast_paced": "Managed complex interfaces between diverse units, streamlining {bold}operational workflows{/bold} and resolving challenges under {bold}strict deadlines{/bold}.",
    "collaborative": "Managed complex interfaces between diverse units, driving {bold}cross-team collaboration{/bold} and resolving challenges with high precision under tight deadlines.",
    "debugging": "Managed complex interfaces between diverse units, identifying and resolving logistical challenges with {bold}analytical precision{/bold} and {bold}systematic problem-solving{/bold}.",
    "default": "Managed complex interfaces between diverse units, streamlining workflows and resolving challenges with precision under tight deadlines.",
}

# ══════════════════════════════════════════════════════════════════════
# 7. VOLUNTEERING & HOBBIES — PERMANENT, NEVER CHANGE
# ══════════════════════════════════════════════════════════════════════

VOLUNTEERING_LINE = "Volunteering: Provided long-term mentoring and support for a child with special needs."
HOBBIES_LINE = "Hobbies: Sports, listening to podcasts, cooking"  # PERMANENT

# ══════════════════════════════════════════════════════════════════════
# 8. LANGUAGES
# ══════════════════════════════════════════════════════════════════════

LANGUAGES_LINE = "Hebrew (native), English (proficient)"

# ══════════════════════════════════════════════════════════════════════
# 9. HARD RULES
# ══════════════════════════════════════════════════════════════════════

BANNED_WORDS = ["Linux", "MATLAB", "SystemVerilog", "UVM", "Specman", "VCS", "Verdi", "Synopsys Design Compiler", "OpenROAD"]
MAX_PROJECTS = 3
SINGLE_PAGE = True

ALL_REAL_SKILLS = [
    "Verilog", "VHDL", "RTL", "Logic Synthesis",
    "Cadence Genus", "Cadence Innovus", "Cadence Virtuoso", "Spectre", "PVS", "Quantus PEX",
    "RTL-to-GDS", "RTL2GDS", "DRC", "LVS", "PEX", "STA",
    "GPDK045", "45nm", "ASIC",
    "Xilinx Vivado", "Kria KR260", "MicroBlaze", "FPGA",
    "Vitis AI", "DPU", "PetaLinux",
    "Full Custom Layout", "Post-Layout Simulation", "PVT Corner",
    "Corner Analysis", "Monte Carlo Simulation",
    "Embedded C", "UART", "GPIO", "SPI", "firmware",
    "board-level bring-up", "HW/SW integration",
    "Python", "Tcl", "PyTorch",
]

# ══════════════════════════════════════════════════════════════════════
# 10. COMPANY DOMAINS
# ══════════════════════════════════════════════════════════════════════

COMPANY_DOMAINS = {
    "nvidia": "next-generation GPU and accelerator silicon",
    "intel": "processor and semiconductor technology",
    "arm": "processor IP and SoC design",
    "qualcomm": "mobile and wireless semiconductor solutions",
    "mobileye": "autonomous driving and ADAS chip technology",
    "annapurna labs": "next-generation cloud silicon and custom processors",
    "cisco": "networking and infrastructure ASIC solutions",
    "hailo": "edge AI processor design",
    "proteantecs": "on-chip monitoring technology for semiconductor reliability",
    "elbit systems": "defense electronics and embedded systems",
    "cadence": "EDA tools and semiconductor IP",
    "siemens eda": "EDA tools and IC verification solutions",
    "valens semiconductor": "high-speed connectivity semiconductor solutions",
    "valens": "high-speed connectivity semiconductor solutions",
    "tower semiconductor": "specialty foundry and analog semiconductor solutions",
    "arbe robotics": "4D imaging radar semiconductor technology",
    "alphawave semi": "high-speed connectivity silicon IP",
    "broadcom": "semiconductor solutions for networking and broadband",
    "marvell": "data infrastructure semiconductor technology",
    "samsung": "advanced semiconductor and memory solutions",
    "tenstorrent": "RISC-V AI silicon",
    "ceremorphic": "AMS and mixed-signal chip design",
    "sandisk": "flash storage and memory controller ASIC design",
    "google": "custom AI and cloud silicon",
    "amazon web services": "custom cloud silicon",
}

# ══════════════════════════════════════════════════════════════════════
# 11. AI PROMPT
# ══════════════════════════════════════════════════════════════════════

def get_cv_generation_prompt(job_title: str, company: str, job_description: str) -> str:
    company_domain = COMPANY_DOMAINS.get(company.lower().strip(), "")
    domain_hint = f"\nKNOWN: {company} works on {company_domain}." if company_domain else ""

    return f"""You are a career consultant crafting a CV for Amos Sarusi applying to "{job_title}" at {company}.
{domain_hint}

STEP 1 — Break the job into: MUST HAVE, DAY TO DAY, SOFT SKILLS, NICE TO HAVE.
STEP 2 — For each keyword: does Amos have it? YES=include, NO=skip.
STEP 3 — Generate content that MIRRORS the job description using THEIR words.

ACTION-VALUE CV METHOD (follow ALL 7 rules strictly):

RULE 1 — TONE:
- BANNED: "proven expertise", "proven ability", "proven track record", "demonstrated capability", "extensive experience", "proficient in methodologies", "track record", "seasoned", "expert in", "hands-on experience". These MUST NOT appear anywhere.
- BANNED: "academic projects", "university projects", "self-taught" — don't label the source.
- Every bullet: STRONG VERB + technical task + MEASURABLE result.
- Verbs: Implemented, Designed, Built, Optimized, Integrated, Debugged, Automated, Identified, Resolved.

RULE 2 — CAR FORMULA (Challenge-Action-Result):
- Per project, one bullet MUST follow: Technical Challenge → Engineering Action → Measurable Result.
- Example: "Identified forwarding logic bottleneck; restructured Verilog RTL, improving WNS by 50ps and converging to 102.3 MHz target."
- This shows problem-solving, not just task execution.

RULE 3 — COMPANY DNA MATCHING:
- Intel: emphasize "engineering discipline", global standards, full silicon lifecycle understanding.
- NVIDIA: emphasize "edge performance", raw power optimization, fast EDA tool learning.
- Other companies: research their identity and match tone accordingly.
- Apply to About section and project emphasis.

RULE 4 — DEEP-TECH TERMINOLOGY (pass ATS + impress team leads):
- "tests" → "corner-case coverage" or "functional verification"
- "physical layout" → "congestion mitigation" or "Clock Tree Synthesis (CTS)"
- "shortening processes" → "EDA Automation" or "Flow Development"
- Use the job description's exact technical terms.

RULE 5 — MILITARY = ENGINEERING TRANSLATION:
- NOT just "commanded". Frame as: "Managed complex technological and optical systems under pressure and uncertainty, leading team in mission-critical operations."
- Maps to: debug under tape-out pressure, cross-team coordination, decision-making with incomplete data.

RULE 6 — NUMERICAL ANCHORS (minimum 3 per project):
- Frequency: 102.3 MHz. Cells: 7,519. Area: 33,064 um2. FPS: 10-12. DRC: zero. Timing violations: zero.
- Every bullet needs at least one hard number.

RULE 7 — ABOUT = "HIGH POTENTIAL" (not skills list):
- Explain HOW he works: "hands-on", "self-driven", "digs into edge cases", "curious about where things break".
- NOT "looking for a job" → "aiming to bring value through [specific thing relevant to company]".
- Sound hungry and curious, not template-generated.

RULE 8 — "SO WHAT?" TEST (every result needs impact):
- After every number/result, explain WHY it matters.
- NOT: "102.3 MHz, 0 violations". YES: "102.3 MHz with 0 violations — clean signoff, tape-out ready".
- NOT: "97% yield". YES: "97% yield across 100 Monte Carlo runs — production-ready design margins".
- NOT: "73% size reduction". YES: "73% size reduction with only 0.06% accuracy loss — efficient edge deployment".

RULE 9 — OWNERSHIP LANGUAGE:
- USE: Led, Owned, Drove, Resolved, Achieved, Delivered, Built, Designed, Implemented.
- NEVER: Performed, Participated in, Assisted, Was involved in, Worked on.

RULE 10 — SYNONYM BOLDING (in the about text, use {{bold}} markers):
- Bold B.Sc. Electrical Engineering ALWAYS.
- Bold Must Have keywords even in About.
- Bold direct synonyms that map to job requirements: troubleshooting→root-cause analysis, verification→signoff, scripting→automation.
- Max 30% bold per section.

AMOS (B.Sc. Electrical Engineering, Ariel University, GPA 84):
- RISC-V processor: Implemented RTL in Verilog across 11 modules with 3 testbenches, ran full RTL2GDS with Cadence Genus/Innovus (45nm), achieved 102.3 MHz / 7,519 cells / 33,064 um2 / zero timing violations / zero DRC. Identified forwarding logic bottleneck, restructured datapath, improved WNS by 50ps. Automated flow with Tcl/Python scripts (EDA Automation).
- Fatigue Detection: Performed full bring-up of real-time detection system on Xilinx Kria KR260, integrated Vitis AI DPU B4096 with MobileNetV2 INT8 quantization, achieved stable 10-12 FPS. Resolved HW/SW integration edge cases during bring-up.
- VLSI Analog Lab: Designed two-stage Op-Amp and digital cells in Cadence Virtuoso 45nm, passed DRC/LVS/PEX, ran corner analysis and Monte Carlo simulations for yield verification.
- MicroBlaze: Built embedded system in Vivado with UART/GPIO/SPI and custom IP blocks, performed full HW/SW bring-up with Embedded C firmware.
- Skills: Verilog, VHDL, Cadence Genus/Innovus/Virtuoso/Spectre/PVS/Quantus, Vivado, Vitis AI, Python, Tcl, Embedded C
- Military: Tank Commander & Deputy Company Sergeant Major, IDF Armored Corps, 2018-2020. Led tank crew under high-pressure conditions with self-discipline and systematic thinking. Managed complex interfaces between diverse units, resolving challenges under tight deadlines.

MANDATORY FIXES:
FIX 1 — RISC-V bullets MUST DIFFER per job type. Never identical across CVs:
  - RTL/Logic Design → microarchitecture, RTL coding, timing closure
  - Verification → testbenches, corner-case coverage, functional verification
  - Physical Design → RTL2GDS flow, P&R, timing analysis, DRC/LVS
  - Integration → multi-module integration, end-to-end flow
FIX 2 — No duplicate bullets. If two bullets say the same thing differently, merge into ONE.
FIX 3 — NEVER include: Synopsys Design Compiler, OpenROAD, or any tool not in the Skills list above.
  Exception: "currently exploring OpenROAD" ONLY if job explicitly requires it.
FIX 4 — For non-relevant projects: keep to 1 line max. If role is Formal Verification, FPGA bullet = 1 short line.
FIX 5 — Military title ALWAYS exact: "Tank Commander & Deputy Company Sergeant Major, IDF Armored Corps, 2018-2020"
FIX 6 — Volunteering always label format: "Volunteering: Provided long-term mentoring..."

GENERATE JSON:

1. "subtitle": Professional title for this role (not exact job title)
2. "about": 3 SHORT sentences as a SINGLE STRING. No bold markers needed.
   - Sentence 1: "Electrical & Electronics Engineering graduate with hands-on experience in [2-3 domains from job]."
   - Sentence 2: "Experienced in taking designs from [start] through [key steps] to [end]." One sentence showing end-to-end.
   - Sentence 3: "Eager to apply [one specific strength] to [one specific challenge] at {company}."
   - Keep it CONCISE. Max 3 sentences total. No fluff.
   - Do NOT list tools in About (tools go in Skills section).
   - STRICT RULES:
     * NO em dashes. NO parentheses. NO curly braces. NO bold markers.
     * NO "proven ability", "proven expertise", "extensive", "comprehensive".
   - NEVER mention: Linux, MATLAB, SystemVerilog, UVM, VCS, Verdi, Specman, Synopsys Design Compiler, OpenROAD
3. "skills_custom": Array of 2-3 {{"label": "...", "content": "..."}} matching job requirements.
   ONLY include tools from Amos's real skills list. NEVER add Synopsys DC, OpenROAD, or tools he hasn't used.
4. "project_order": Array of 3 keys from ["riscv", "fatigue", "vlsi_lab", "microblaze"]
   Order by relevance to THIS specific job. Reorder for every job.
   Examples: Verification/RTL→riscv first, FPGA/Embedded→fatigue first, PD/Analog→vlsi_lab first.
5. "project_expansion": {{"key": "full"/"medium"/"compressed"}} for each.
   "full"=3 CAR bullets, "medium"=2 bullets, "compressed"=1 line.
   MANDATORY: "riscv" and "fatigue" MUST ALWAYS be "full" (3 bullets each). They are the two strongest projects.
   Only "vlsi_lab" and "microblaze" can be "medium" or "compressed".
6. "military_tone": one of "innovative", "independent", "fast_paced", "collaborative", "debugging", "default"
7. "coursework": one of "verification", "asic_rtl", "fpga_embedded", "physical_design", "analog", "application", "general"

JOB DESCRIPTION:
{job_description[:2000]}

JSON only, no markdown."""
