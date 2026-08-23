"""
Generate Dynamic Programming Revision Guide PDF
"""
from fpdf import FPDF
import os

class DPRevisionPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
    
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(100, 100, 100)
            self.cell(0, 5, "Dynamic Programming - FAANG Interview Revision Guide", align="C")
            self.ln(8)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")
    
    def title_page(self):
        self.add_page()
        self.ln(60)
        self.set_font("Helvetica", "B", 36)
        self.set_text_color(25, 25, 112)
        self.cell(0, 20, "Dynamic Programming", align="C")
        self.ln(20)
        self.set_font("Helvetica", "B", 28)
        self.set_text_color(70, 70, 70)
        self.cell(0, 15, "FAANG Interview", align="C")
        self.ln(15)
        self.cell(0, 15, "Revision Guide", align="C")
        self.ln(25)
        self.set_font("Helvetica", "", 14)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, "Knapsack  |  LCS  |  MCM  |  Standalone DP", align="C")
        self.ln(10)
        self.cell(0, 10, "Tricks, Patterns, Templates & Questions", align="C")
        self.ln(30)
        self.set_draw_color(25, 25, 112)
        self.set_line_width(0.8)
        self.line(40, self.get_y(), 170, self.get_y())
        self.ln(10)
        self.set_font("Helvetica", "I", 11)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, "Complete guide with Recursion, Memoization & Bottom-Up for every problem", align="C")
        self.ln(8)
        self.cell(0, 8, "From basic identification to advanced FAANG-level optimizations", align="C")
    
    def chapter_title(self, title, subtitle=""):
        self.add_page()
        self.ln(5)
        self.set_fill_color(25, 25, 112)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 20)
        self.cell(0, 14, f"  {title}", fill=True)
        self.ln(16)
        if subtitle:
            self.set_text_color(80, 80, 80)
            self.set_font("Helvetica", "I", 11)
            self.cell(0, 8, subtitle)
            self.ln(10)
    
    def section_title(self, title):
        self.ln(4)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(25, 25, 112)
        self.cell(0, 8, title)
        self.ln(8)
        self.set_draw_color(25, 25, 112)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
    
    def sub_section(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(50, 50, 50)
        self.cell(0, 7, title)
        self.ln(8)
    
    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(2)
    
    def bold_text(self, text):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(1)
    
    def trick_box(self, title, content):
        self.ln(2)
        y_start = self.get_y()
        if y_start > 255:
            self.add_page()
            y_start = self.get_y()
        self.set_fill_color(255, 248, 220)
        self.set_draw_color(218, 165, 32)
        self.set_line_width(0.5)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(139, 90, 0)
        self.cell(0, 7, f"  TRICK: {title}", fill=True, border=1)
        self.ln(8)
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(80, 60, 0)
        x = self.get_x()
        self.set_x(x + 3)
        self.multi_cell(184, 5, content)
        self.ln(3)
    
    def code_block(self, code):
        self.ln(1)
        self.set_fill_color(240, 240, 245)
        self.set_font("Courier", "", 8.5)
        self.set_text_color(30, 30, 30)
        lines = code.strip().split('\n')
        for line in lines:
            if self.get_y() > 270:
                self.add_page()
            safe = line.replace('\t', '    ')
            self.cell(0, 4.5, f"  {safe}", fill=True)
            self.ln(4.5)
        self.ln(3)
    
    def table_row(self, cells, widths, header=False):
        if self.get_y() > 270:
            self.add_page()
        if header:
            self.set_font("Helvetica", "B", 8.5)
            self.set_fill_color(25, 25, 112)
            self.set_text_color(255, 255, 255)
        else:
            self.set_font("Helvetica", "", 8.5)
            self.set_fill_color(245, 245, 250)
            self.set_text_color(40, 40, 40)
        for i, (cell, w) in enumerate(zip(cells, widths)):
            self.cell(w, 6.5, f" {cell}", border=1, fill=True)
        self.ln(6.5)
    
    def bullet(self, text, indent=0):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        x = 15 + indent
        self.set_x(x)
        self.cell(5, 5.5, chr(8226))
        self.multi_cell(180 - indent, 5.5, text)
        self.ln(1)
    
    def keyword_box(self, items):
        self.ln(1)
        self.set_fill_color(232, 245, 233)
        self.set_draw_color(76, 175, 80)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(27, 94, 32)
        for item in items:
            if self.get_y() > 270:
                self.add_page()
            self.cell(0, 5.5, f"    {item}", fill=True, border="L")
            self.ln(5.5)
        self.ln(3)

    def formula_box(self, formula):
        self.ln(2)
        if self.get_y() > 265:
            self.add_page()
        self.set_fill_color(230, 240, 255)
        self.set_draw_color(25, 25, 112)
        self.set_font("Courier", "B", 10)
        self.set_text_color(25, 25, 112)
        self.cell(0, 8, f"    {formula}", fill=True, border=1)
        self.ln(10)

    def problem_header(self, num, title, difficulty, companies):
        self.ln(4)
        if self.get_y() > 250:
            self.add_page()
        self.set_fill_color(63, 81, 181)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 9, f"  Problem {num}: {title}  [{difficulty}]", fill=True)
        self.ln(10)
        self.set_font("Helvetica", "I", 8.5)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, f"Companies: {companies}")
        self.ln(7)

    # ── diagram drawing helpers ──────────────────────────────────────────
    def _box(self, x, y, w, h, text, fill_rgb, text_rgb=(255,255,255),
             font_size=7, border_rgb=None, bold=True):
        """Draw a rounded-corner-ish box with centered text."""
        self.set_fill_color(*fill_rgb)
        if border_rgb:
            self.set_draw_color(*border_rgb)
        else:
            self.set_draw_color(*fill_rgb)
        self.set_line_width(0.4)
        self.rect(x, y, w, h, style="FD")
        self.set_text_color(*text_rgb)
        self.set_font("Helvetica", "B" if bold else "", font_size)
        self.set_xy(x, y)
        self.cell(w, h, text, align="C")

    def _arrow_down(self, x1, y1, x2, y2, color=(120,120,120)):
        self.set_draw_color(*color)
        self.set_line_width(0.35)
        self.line(x1, y1, x2, y2)
        # arrowhead
        self.line(x2 - 1.2, y2 - 2, x2, y2)
        self.line(x2 + 1.2, y2 - 2, x2, y2)

    def _arrow_right(self, x1, y1, x2, y2, color=(120,120,120)):
        self.set_draw_color(*color)
        self.set_line_width(0.35)
        self.line(x1, y1, x2, y2)

    def draw_family_overview_diagram(self):
        """Page 1: The 4 DP families overview tree."""
        self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(25, 25, 112)
        self.cell(0, 10, "DP Family Architecture Diagram", align="C")
        self.ln(14)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100,100,100)
        self.cell(0, 5, "Master map: 4 patterns, 41 problems, all from 4 templates", align="C")
        self.ln(12)

        # Root node
        self._box(60, 42, 80, 12, "DYNAMIC PROGRAMMING", (25,25,112))

        # Vertical line down from root
        self.set_draw_color(25,25,112)
        self.set_line_width(0.5)
        self.line(100, 54, 100, 62)

        # Horizontal connector
        self.line(25, 62, 175, 62)

        # 4 vertical drops
        for x in [25, 75, 125, 175]:
            self.line(x, 62, x, 68)

        # 4 family boxes
        families = [
            (5, "0/1 Knapsack", (33,150,83)),
            (55, "Unbounded KS", (255,152,0)),
            (105, "LCS", (63,81,181)),
            (155, "MCM", (156,39,176)),
        ]
        for x, name, color in families:
            self._box(x, 68, 40, 10, name, color, font_size=7)

        # ── 0/1 KNAPSACK children ────────────────────────────────
        ks_children = ["0/1 Knapsack", "Subset Sum", "Equal Partition",
                       "Count Subsets", "Min Subset Diff", "Target Sum",
                       "#Subsets Diff"]
        base_y = 84
        for i, name in enumerate(ks_children):
            y = base_y + i * 8.5
            self._box(2, y, 44, 7, name, (232,245,233), (27,94,32),
                      font_size=6, border_rgb=(76,175,80), bold=False)
        self.line(25, 78, 25, base_y)
        for i in range(len(ks_children)):
            self.set_draw_color(76,175,80)
            self.set_line_width(0.3)
            self.line(25, base_y + i*8.5, 25, base_y + i*8.5 + 3.5)

        # ── UNBOUNDED children ────────────────────────────────────
        ub_children = ["Rod Cutting", "Coin Change Ways", "Coin Change Min",
                       "Integer Break", "Perfect Squares", "Min Cost Tickets",
                       "Word Break", "Word Break Count", "Combo Sum IV"]
        for i, name in enumerate(ub_children):
            y = base_y + i * 8.5
            self._box(50, y, 44, 7, name, (255,243,224), (230,81,0),
                      font_size=6, border_rgb=(255,152,0), bold=False)
        self.line(75, 78, 75, base_y)

        # ── LCS children ──────────────────────────────────────────
        lcs_children = ["LCS", "Common Substring", "Print LCS / SCS",
                        "Min Insert+Delete", "Repeating Subseq",
                        "Palindrome Subseq", "Palindrome Substr",
                        "Edit Distance", "Interleaving Str"]
        for i, name in enumerate(lcs_children):
            y = base_y + i * 8.5
            self._box(98, y, 44, 7, name, (227,236,255), (25,25,112),
                      font_size=6, border_rgb=(63,81,181), bold=False)
        self.line(125, 78, 125, base_y)

        # ── MCM children ──────────────────────────────────────────
        mcm_children = ["MCM", "Palindrome Part.", "Boolean Parenth.",
                        "Scramble String", "Egg Dropping", "Burst Balloons",
                        "Merge Stones", "Polygon Triang."]
        for i, name in enumerate(mcm_children):
            y = base_y + i * 8.5
            self._box(146, y, 44, 7, name, (243,229,245), (106,27,154),
                      font_size=6, border_rgb=(156,39,176), bold=False)
        self.line(175, 78, 175, base_y)

        # ── Legend ────────────────────────────────────────────────
        ly = 170
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(60,60,60)
        self.set_xy(10, ly)
        self.cell(0, 5, "Total: 7 + 9 + 9 + 8 = 33 core problems  (+8 standalone = 41 problems)")

    def draw_standalone_diagram(self):
        """Page 2: Standalone DP problems diagram."""
        self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(25, 25, 112)
        self.cell(0, 10, "Standalone DP Problems Map", align="C")
        self.ln(14)

        # Root
        self._box(55, 38, 90, 12, "STANDALONE DP", (96,125,139))

        self.set_draw_color(96,125,139)
        self.set_line_width(0.5)
        self.line(100, 50, 100, 58)
        self.line(20, 58, 180, 58)

        problems = [
            (5, "Count Ways\n(Fibonacci)", (0,150,136)),
            (37, "Jump Game\n(Greedy)", (244,67,54)),
            (69, "House Robber\n(Linear DP)", (63,81,181)),
            (101, "Knight Dialer\n(Graph DP)", (156,39,176)),
            (133, "Largest Square\n(Matrix DP)", (255,152,0)),
            (165, "Word Wrap\n(Partition)", (33,150,83)),
        ]

        for x, name, color in problems:
            self.line(x + 16, 58, x + 16, 65)
            lines = name.split('\n')
            self._box(x, 65, 32, 9, lines[0], color, font_size=6.5)
            self._box(x, 74, 32, 7, lines[1], (240,240,240), (80,80,80),
                      font_size=5.5, bold=False)

        # Key formulas under each
        formulas = [
            (5, "dp[i]=dp[i-1]+dp[i-2]"),
            (37, "track farthest pos"),
            (69, "max(a[i]+dp[i-2],dp[i-1])"),
            (101, "sum(dp[prev_digits])"),
            (133, "1+min(top,left,diag)"),
            (165, "min(cost+dp[j+1])"),
        ]
        for x, f in formulas:
            self.set_font("Courier", "", 5)
            self.set_text_color(80,80,80)
            self.set_xy(x, 83)
            self.cell(32, 4, f, align="C")

        # Approach boxes
        self.ln(10)
        y = 95
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(25,25,112)
        self.set_xy(10, y)
        self.cell(0, 6, "Each Problem Has 4 Approaches:")
        y += 10

        approaches = [
            ("1. Recursion", "(Brute Force)", (244,67,54)),
            ("2. Memoization", "(Top-Down DP)", (255,152,0)),
            ("3. Bottom-Up", "(Tabulation)", (33,150,83)),
            ("4. Space Optimized", "(O(1) or O(n))", (25,25,112)),
        ]
        for i, (title, sub, color) in enumerate(approaches):
            bx = 12 + i * 47
            self._box(bx, y, 44, 9, title, color, font_size=7)
            self._box(bx, y + 9, 44, 7, sub, (240,240,240), (80,80,80),
                      font_size=6, bold=False)

        # arrows between approaches
        for i in range(3):
            x1 = 12 + i * 47 + 44
            x2 = 12 + (i+1) * 47
            mid_y = y + 6
            self.set_draw_color(120,120,120)
            self.set_line_width(0.3)
            self.line(x1, mid_y, x2, mid_y)
            self.line(x2 - 1.5, mid_y - 1, x2, mid_y)
            self.line(x2 - 1.5, mid_y + 1, x2, mid_y)

    def draw_approach_flow_diagram(self):
        """Page 3: Recursion -> Memo -> Bottom-Up flow with what changes."""
        self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(25, 25, 112)
        self.cell(0, 10, "The DP Conversion Pipeline", align="C")
        self.ln(14)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100,100,100)
        self.cell(0, 5, "How to convert any recursive solution to optimal DP in 3 steps", align="C")
        self.ln(14)

        # 3 big boxes: Recursion -> Memo -> Bottom-Up
        y = 50
        box_w, box_h = 50, 18

        # Recursion box
        self._box(10, y, box_w, box_h, "RECURSION", (244,67,54), font_size=10)
        # what it does
        self.set_font("Helvetica", "", 7)
        self.set_text_color(60,60,60)
        steps_r = ["Base case + Choice", "Try all options", "O(2^n) time"]
        for i, s in enumerate(steps_r):
            self.set_xy(10, y + box_h + 2 + i * 5)
            self.cell(box_w, 4, s, align="C")

        # Arrow 1
        self.set_draw_color(80,80,80)
        self.set_line_width(0.5)
        self.line(60, y + 9, 75, y + 9)
        self.line(73, y + 7, 75, y + 9)
        self.line(73, y + 11, 75, y + 9)
        self.set_font("Helvetica", "B", 6)
        self.set_text_color(244,67,54)
        self.set_xy(61, y + 1)
        self.cell(13, 5, "+3 lines", align="C")

        # Memo box
        self._box(75, y, box_w, box_h, "MEMOIZATION", (255,152,0), font_size=10)
        steps_m = ["Add cache check", "Store before return", "O(n*W) or O(n^2)"]
        for i, s in enumerate(steps_m):
            self.set_xy(75, y + box_h + 2 + i * 5)
            self.set_font("Helvetica", "", 7)
            self.set_text_color(60,60,60)
            self.cell(box_w, 4, s, align="C")

        # Arrow 2
        self.set_draw_color(80,80,80)
        self.line(125, y + 9, 140, y + 9)
        self.line(138, y + 7, 140, y + 9)
        self.line(138, y + 11, 140, y + 9)
        self.set_font("Helvetica", "B", 6)
        self.set_text_color(255,152,0)
        self.set_xy(126, y + 1)
        self.cell(13, 5, "loops", align="C")

        # Bottom-Up box
        self._box(140, y, box_w, box_h, "BOTTOM-UP", (33,150,83), font_size=10)
        steps_b = ["Replace recursion", "Fill table iteratively", "O(n*W) + space opt"]
        for i, s in enumerate(steps_b):
            self.set_xy(140, y + box_h + 2 + i * 5)
            self.set_font("Helvetica", "", 7)
            self.set_text_color(60,60,60)
            self.cell(box_w, 4, s, align="C")

        # ── Per-family filling strategy ──────────────────────────
        y2 = 100
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(25,25,112)
        self.set_xy(10, y2)
        self.cell(0, 8, "How Each Family Fills the DP Table")
        y2 += 14

        families_fill = [
            ("0/1 KNAPSACK", "Row by row (i = items, j = capacity)\nj: RIGHT to LEFT in 1D\ndp[i-1] = previous row",
             (33,150,83)),
            ("UNBOUNDED KS", "Row by row (i = items, j = capacity)\nj: LEFT to RIGHT in 1D\ndp[i] = SAME row (reuse!)",
             (255,152,0)),
            ("LCS", "Row by row (i = string1, j = string2)\nMatch: diagonal +1, Mismatch: max(up,left)\nSpace: 2 rows only",
             (63,81,181)),
            ("MCM", "DIAGONAL by gap size (gap = j - i)\nSmall gaps first, then larger\nCannot reduce to 1D!",
             (156,39,176)),
        ]

        for title, desc, color in families_fill:
            if self.get_y() > 260:
                self.add_page()
            self._box(10, y2, 35, 9, title, color, font_size=7)
            self.set_font("Helvetica", "", 7.5)
            self.set_text_color(50,50,50)
            lines = desc.split('\n')
            for li, l in enumerate(lines):
                self.set_xy(48, y2 + 1 + li * 4)
                self.cell(140, 4, l)
            y2 += max(len(lines) * 4 + 5, 14)

        # ── Key conversion rules ──────────────────────────────────
        y3 = y2 + 8
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(25,25,112)
        self.set_xy(10, y3)
        self.cell(0, 8, "Conversion Rules (Recursion to Bottom-Up)")
        y3 += 12

        rules = [
            "Base case  if n==0: return 0   -->   dp[0][j] = 0  (first row/col init)",
            "Recursive call  f(n-1, w)      -->   dp[i-1][j]    (table lookup)",
            "Return value  return max(a,b)  -->   dp[i][j] = max(a,b)  (store in cell)",
            "Changing vars  (n, w)          -->   loop dimensions  (i, j)",
            "Function call  f(i,k)+f(k+1,j) -->  dp[i][k]+dp[k+1][j]  (MCM style)",
        ]
        for r in rules:
            self.set_fill_color(245,245,250)
            self.set_draw_color(25,25,112)
            self.set_font("Courier", "", 7)
            self.set_text_color(30,30,30)
            self.set_xy(10, y3)
            self.cell(185, 5.5, f"  {r}", fill=True, border="L")
            y3 += 6.5

    def draw_knapsack_vs_unbounded_diagram(self):
        """Page 4: Visual comparison of 0/1 vs Unbounded Knapsack."""
        self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(25, 25, 112)
        self.cell(0, 10, "0/1 vs Unbounded Knapsack: Visual Difference", align="C")
        self.ln(14)

        y = 40

        # ── 0/1 Knapsack side ──
        self._box(10, y, 85, 10, "0/1 KNAPSACK", (33,150,83), font_size=10)
        y1 = y + 14

        # 2D grid showing dp[i-1] usage
        self.set_font("Helvetica", "B", 7)
        self.set_text_color(33,150,83)
        self.set_xy(10, y1)
        self.cell(85, 5, "Uses dp[i-1][j-wt] = PREVIOUS ROW", align="C")
        y1 += 8

        # Draw mini grid
        for row in range(4):
            for col in range(6):
                bx = 18 + col * 12
                by = y1 + row * 8
                if row == 2 and col == 4:
                    self._box(bx, by, 11, 7, "dp[i][j]", (33,150,83), font_size=5)
                elif row == 1 and col == 2:
                    self._box(bx, by, 11, 7, "USED", (76,175,80), font_size=5)
                elif row == 1 and col == 4:
                    self._box(bx, by, 11, 7, "USED", (76,175,80), font_size=5)
                else:
                    self._box(bx, by, 11, 7, "", (240,240,240), border_rgb=(200,200,200))
        # arrows from prev row
        self.set_draw_color(33,150,83)
        self.set_line_width(0.5)
        self.line(42+5, y1+8+7, 66+5, y1+16)  # diagonal from dp[i-1][j-wt]
        self.line(66+5, y1+8+7, 66+5, y1+16)  # from dp[i-1][j]

        y1 += 38
        self.set_font("Courier", "B", 8)
        self.set_text_color(33,150,83)
        self.set_xy(10, y1)
        self.cell(85, 5, "1D: j from W DOWN TO wt[i]", align="C")
        y1 += 6
        self.set_xy(10, y1)
        self.cell(85, 5, "(RIGHT to LEFT)", align="C")

        # ── Unbounded side ──
        y2 = y
        self._box(105, y2, 85, 10, "UNBOUNDED KNAPSACK", (255,152,0), font_size=10)
        y2 = y + 14

        self.set_font("Helvetica", "B", 7)
        self.set_text_color(255,152,0)
        self.set_xy(105, y2)
        self.cell(85, 5, "Uses dp[i][j-wt] = SAME ROW", align="C")
        y2 += 8

        # Draw mini grid
        for row in range(4):
            for col in range(6):
                bx = 113 + col * 12
                by = y2 + row * 8
                if row == 2 and col == 4:
                    self._box(bx, by, 11, 7, "dp[i][j]", (255,152,0), font_size=5)
                elif row == 2 and col == 2:
                    self._box(bx, by, 11, 7, "USED", (255,183,77), (0,0,0), font_size=5)
                elif row == 1 and col == 4:
                    self._box(bx, by, 11, 7, "USED", (255,183,77), (0,0,0), font_size=5)
                else:
                    self._box(bx, by, 11, 7, "", (240,240,240), border_rgb=(200,200,200))
        # arrows from same row
        self.set_draw_color(255,152,0)
        self.set_line_width(0.5)
        self.line(137+5, y2+16+3, 161+5, y2+16+3)  # from dp[i][j-wt] same row
        self.line(161+5, y2+8+7, 161+5, y2+16)      # from dp[i-1][j]

        y2 += 38
        self.set_font("Courier", "B", 8)
        self.set_text_color(255,152,0)
        self.set_xy(105, y2)
        self.cell(85, 5, "1D: j from wt[i] UP TO W", align="C")
        y2 += 6
        self.set_xy(105, y2)
        self.cell(85, 5, "(LEFT to RIGHT)", align="C")

        # ── The ONE character difference ──
        yd = max(y1, y2) + 14
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(25,25,112)
        self.set_xy(10, yd)
        self.cell(0, 7, "The ONE Character Difference:")
        yd += 10

        self.set_fill_color(245,245,250)
        self.set_draw_color(33,150,83)
        self.set_font("Courier", "B", 9)
        self.set_text_color(33,150,83)
        self.set_xy(10, yd)
        self.cell(185, 7, "  0/1:       val[i-1] + dp[i-1][j-wt[i-1]]   <-- i-1 (GO to prev row)", fill=True, border="L")
        yd += 9
        self.set_draw_color(255,152,0)
        self.set_text_color(255,152,0)
        self.set_xy(10, yd)
        self.cell(185, 7, "  Unbounded: val[i-1] + dp[ i ][j-wt[i-1]]   <-- i   (STAY on same row)", fill=True, border="L")

    def draw_mcm_diagonal_diagram(self):
        """Page 5: MCM diagonal filling visualization."""
        self.add_page()
        self.ln(2)
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(25, 25, 112)
        self.cell(0, 10, "MCM: Diagonal Table Filling", align="C")
        self.ln(14)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100,100,100)
        self.cell(0, 5, "Unlike Knapsack (row-by-row), MCM fills by GAP SIZE along diagonals", align="C")
        self.ln(14)

        y = 50
        n = 5  # 5x5 grid
        cell_size = 18
        start_x = 45

        # Column headers
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(60,60,60)
        for j in range(n):
            self.set_xy(start_x + j * cell_size + 3, y - 6)
            self.cell(cell_size - 6, 5, f"j={j}", align="C")

        # Row headers
        for i in range(n):
            self.set_xy(start_x - 12, y + i * cell_size + 5)
            self.cell(10, 5, f"i={i}", align="R")

        # Color scheme for diagonals
        colors = [
            (76,175,80),     # gap 0 - green
            (33,150,243),    # gap 1 - blue
            (255,152,0),     # gap 2 - orange
            (244,67,54),     # gap 3 - red
            (156,39,176),    # gap 4 - purple
        ]

        fill_order = 1
        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                bx = start_x + j * cell_size
                by = y + i * cell_size
                if i <= j:
                    color = colors[gap]
                    label = str(fill_order)
                    self._box(bx, by, cell_size - 1, cell_size - 1, label,
                              color, font_size=8)
                    fill_order += 1
                else:
                    self._box(bx, by, cell_size - 1, cell_size - 1, "",
                              (230,230,230), border_rgb=(200,200,200))

        # Grey out lower triangle
        for i in range(n):
            for j in range(i):
                bx = start_x + j * cell_size
                by = y + i * cell_size
                self._box(bx, by, cell_size - 1, cell_size - 1, "-",
                          (230,230,230), (180,180,180),
                          font_size=8, border_rgb=(200,200,200), bold=False)

        # Legend
        ly = y + n * cell_size + 10
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(25,25,112)
        self.set_xy(10, ly)
        self.cell(0, 6, "Fill Order by Gap Size:")
        ly += 8

        gap_labels = ["Gap 0 (diagonal - base)", "Gap 1 (pairs)",
                      "Gap 2 (triples)", "Gap 3 (quads)", "Gap 4 (full range = ANSWER)"]
        for i, (label, color) in enumerate(zip(gap_labels, colors)):
            self._box(15, ly, 8, 6, "", color)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(60,60,60)
            self.set_xy(25, ly)
            self.cell(80, 6, label)
            ly += 8

        # Code
        ly += 5
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(25,25,112)
        self.set_xy(10, ly)
        self.cell(0, 6, "The Diagonal Filling Loop:")
        ly += 8

        self.set_font("Courier", "", 8)
        self.set_fill_color(240,240,245)
        self.set_text_color(30,30,30)
        code_lines = [
            "for gap in range(1, n):         # gap = j - i",
            "    for i in range(n - gap):     # starting index",
            "        j = i + gap",
            "        dp[i][j] = INF",
            "        for k in range(i, j):   # try all split points",
            "            cost = dp[i][k] + dp[k+1][j] + merge_cost",
            "            dp[i][j] = min(dp[i][j], cost)",
        ]
        for line in code_lines:
            self.set_xy(15, ly)
            self.cell(170, 5, f"  {line}", fill=True)
            ly += 5.5


def build_pdf():
    pdf = DPRevisionPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # =========================================================================
    # TITLE PAGE
    # =========================================================================
    pdf.title_page()

    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(25, 25, 112)
    pdf.cell(0, 15, "Table of Contents")
    pdf.ln(20)

    toc = [
        ("Chapter 1: The DP Masterplan", "How to identify & solve ANY DP problem"),
        ("Chapter 2: 0/1 Knapsack Family", "7 problems from one template"),
        ("Chapter 3: Unbounded Knapsack Family", "10 problems including Rod Cut, Coin Change, Word Break"),
        ("Chapter 4: LCS Family", "16 problems including Edit Distance, Palindromes"),
        ("Chapter 5: MCM / Partition DP Family", "8 problems including Burst Balloons, Egg Drop"),
        ("Chapter 6: Standalone DP Problems", "Count Ways, Jump Game, House Robber, Knight Dialer, etc."),
        ("Chapter 7: Ultimate Cheat Sheet", "All formulas, patterns & tricks on one page"),
        ("Chapter 8: Visual Architecture Diagrams", "Family trees, conversion flows, table filling visuals"),
    ]
    for i, (title, desc) in enumerate(toc):
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(0, 8, title)
        pdf.ln(7)
        pdf.set_font("Helvetica", "I", 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 6, f"    {desc}")
        pdf.ln(10)

    # =========================================================================
    # CHAPTER 1: THE DP MASTERPLAN
    # =========================================================================
    pdf.chapter_title("Chapter 1: The DP Masterplan",
                      "How to identify and solve ANY Dynamic Programming problem in interviews")

    pdf.section_title("The 4 DP Families (Learn 4 templates, solve 40+ problems)")
    
    w = [48, 48, 48, 48]
    pdf.table_row(["Family", "# Problems", "Key Idea", "Identification"], w, header=True)
    pdf.table_row(["0/1 Knapsack", "7", "Pick or Skip", "Choice + Capacity"], w)
    pdf.table_row(["Unbounded KS", "10", "Reuse items", "Infinite supply"], w)
    pdf.table_row(["LCS", "16", "Two string compare", "Common/Convert"], w)
    pdf.table_row(["MCM", "8", "Split range at k", "Partition range"], w)

    pdf.section_title("The 3-Step Recipe (works for EVERY DP problem)")
    pdf.bold_text("Step 1: Write RECURSION with base case + choice diagram")
    pdf.body_text("Think: 'What choices do I have at each step?' Write the brute force.")
    pdf.bold_text("Step 2: Add MEMOIZATION (cache changing variables)")
    pdf.body_text("Find variables that change in recursion. Create dp table. Add 3 lines: check cache, compute, store.")
    pdf.bold_text("Step 3: Convert to BOTTOM-UP (tabulation)")
    pdf.body_text("Replace recursion with loops. Base case becomes initialization. Recursive calls become table lookups.")

    pdf.section_title("How to Identify DP in 5 Seconds")
    pdf.keyword_box([
        '"maximize/minimize" + "choices at each step" --> DP',
        '"count number of ways" --> DP',
        '"can you reach / is it possible" --> DP',
        '"optimal substructure" + "overlapping subproblems" --> DP',
        'Greedy FAILS (need to try all combinations) --> DP',
    ])

    pdf.section_title("Recursion to Memoization (3 Lines Added)")
    pdf.code_block("""# Line 1: Create memo table
memo = {}  # or memo[n+1][w+1] = -1

# Line 2: Check before computing
if key in memo: return memo[key]

# Line 3: Store before returning  
memo[key] = result
return memo[key]""")

    pdf.section_title("Memoization to Bottom-Up Conversion")
    pdf.trick_box("Base case in recursion = Initialization in Bottom-Up",
                  "if n==0: return 0  -->  dp[0][j] = 0 for all j\n"
                  "Recursive call f(n-1, w) --> dp[i-1][j] in table\n"
                  "The changing variables (n, w) become loop dimensions (i, j)")

    # =========================================================================
    # CHAPTER 2: 0/1 KNAPSACK
    # =========================================================================
    pdf.chapter_title("Chapter 2: 0/1 Knapsack Family",
                      "7 problems from ONE template - Learn once, solve all")

    pdf.section_title("Identification: How to spot Knapsack in 5 seconds")
    pdf.keyword_box([
        'Question 1: "Am I making a PICK or SKIP choice for each item?"  --> YES',
        'Question 2: "Is there a CONSTRAINT (capacity, sum, limit)?"  --> YES',
        'BOTH YES = Knapsack Family!',
        '"Pick or Skip" + "Constraint" = KNAPSACK',
    ])

    pdf.section_title("The Choice Diagram (draw this in EVERY interview)")
    pdf.code_block("""        item i (weight = wt[i], value = val[i])
               /                    \\
        wt[i] <= W?              wt[i] > W?
        (CAN pick)               (TOO heavy)
         /        \\                   |
       PICK      SKIP               SKIP
    val[i] +     solve(W,        solve(W, n-1)
    solve(W -    n-1)
    wt[i], n-1)

    Answer = max(PICK, SKIP)  if can pick
    Answer = SKIP             if too heavy""")

    pdf.section_title("The Universal Template")
    pdf.code_block("""def knapsack(wt, val, w, n):
    if n == 0 or w == 0:
        return 0
    if wt[n-1] <= w:
        pick = val[n-1] + knapsack(wt, val, w - wt[n-1], n-1)
        skip = knapsack(wt, val, w, n-1)
        return max(pick, skip)
    else:
        return knapsack(wt, val, w, n-1)""")

    pdf.section_title("Bottom-Up Template")
    pdf.code_block("""dp[i][j] = 0  for i=0 or j=0  (base case)

for i in range(1, n+1):
    for j in range(1, W+1):
        if wt[i-1] <= j:
            dp[i][j] = max(val[i-1] + dp[i-1][j - wt[i-1]],  # pick
                           dp[i-1][j])                          # skip
        else:
            dp[i][j] = dp[i-1][j]                               # must skip""")

    pdf.section_title("The 7 Knapsack Children (all from same template)")
    w = [38, 20, 20, 30, 30, 52]
    pdf.table_row(["Problem", "dp type", "Operator", "Target (W)", "LC #", "Key Change"], w, header=True)
    pdf.table_row(["0/1 Knapsack", "int", "max()", "capacity", "-", "Base problem"], w)
    pdf.table_row(["Subset Sum", "bool", "OR", "target S", "-", "Can we reach sum?"], w)
    pdf.table_row(["Equal Partition", "bool", "OR", "sum/2", "416", "totalSum must be even"], w)
    pdf.table_row(["Count Subsets", "int", "  +", "target S", "-", "How many subsets?"], w)
    pdf.table_row(["Min Subset Diff", "bool", "OR", "all sums", "1049", "min(total - 2*S1)"], w)
    pdf.table_row(["Target Sum", "int", "  +", "(T+tgt)/2", "494", "+/- assignment"], w)
    pdf.table_row(["#Subsets Diff", "int", "  +", "(T+diff)/2", "-", "S1 - S2 = diff"], w)

    pdf.trick_box("3 types of operators",
                  '"Can we?" (yes/no) --> bool, use OR  (Subset Sum, Partition)\n'
                  '"How many?" (count) --> int, use +   (Count Subsets, Target Sum)\n'
                  '"Best value?" (optimize) --> int, use max()  (Knapsack)')

    pdf.section_title("Space Optimization: O(n*W) to O(W)")
    pdf.trick_box("1D Array - RIGHT to LEFT",
                  "for i in range(n):\n"
                  "    for j in range(W, wt[i]-1, -1):  # RIGHT to LEFT!\n"
                  "        dp[j] = max(dp[j], val[i] + dp[j - wt[i]])\n\n"
                  "WHY right to left? Left to right would use updated values = using item TWICE!")

    # =========================================================================
    # CHAPTER 3: UNBOUNDED KNAPSACK
    # =========================================================================
    pdf.chapter_title("Chapter 3: Unbounded Knapsack Family",
                      "10 problems - 'Infinite supply' = stay on same row")

    pdf.section_title("The ONE-CHARACTER Difference from 0/1 Knapsack")
    pdf.formula_box("0/1:       dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])")
    pdf.formula_box("Unbounded: dp[i][j] = max(val[i-1] + dp[i][j-wt[i-1]],  dp[i-1][j])")
    pdf.trick_box("STAY vs GO",
                  "0/1 Knapsack: GO to previous row (i-1) -- item used ONCE, move on\n"
                  "Unbounded:    STAY on same row (i)     -- item can be REUSED!\n\n"
                  "Memory: 'Unbounded = Unlimited = U stay on same row'")

    pdf.section_title("Identification: How to know it's UNBOUNDED?")
    pdf.keyword_box([
        '"infinite supply" --> UNBOUNDED',
        '"unlimited quantity" --> UNBOUNDED', 
        '"can use multiple times" --> UNBOUNDED',
        '"at most once" --> 0/1 Knapsack',
    ])

    pdf.section_title("1D Space Optimization: LEFT to RIGHT")
    pdf.trick_box("Direction matters!",
                  "0/1 Knapsack 1D:  j from RIGHT to LEFT  (W down to wt[i])\n"
                  "Unbounded 1D:     j from LEFT to RIGHT   (wt[i] up to W)\n\n"
                  "LEFT-to-RIGHT uses updated values = reusing same item (unbounded!)\n"
                  "RIGHT-to-LEFT uses old values = item used only once (0/1)")

    pdf.section_title("The 10 Unbounded Problems")
    
    problems = [
        ("Rod Cutting", "length[]", "price[]", "rod_len", "MAX profit"),
        ("Coin Change Ways", "coins[]", "1 each", "target", "COUNT ways"),
        ("Coin Change Min", "coins[]", "1 each", "target", "MIN coins"),
        ("Integer Break", "[1..n-1]", "products", "n", "MAX product"),
        ("Perfect Squares", "[1,4,9..]", "1 each", "n", "MIN count"),
        ("Min Cost Tickets", "[1,7,30]", "costs[]", "max_day", "MIN cost"),
        ("Max Ribbon Cut", "cuts[]", "1 each", "length", "MAX pieces"),
        ("Word Break", "words[]", "bool", "len(s)", "Feasible?"),
        ("Word Break Count", "words[]", "1 each", "len(s)", "COUNT ways"),
        ("Combo Sum IV", "nums[]", "1 each", "target", "COUNT perms"),
    ]
    w = [32, 24, 22, 22, 26, 28, 36]
    pdf.table_row(["Problem", "items", "values", "capacity", "Optimize", "LC #", "Key Trick"], w, header=True)
    data = [
        ["Rod Cutting", "length[]", "price[]", "rod_len", "MAX", "-", "lengths are weights"],
        ["Coin Change I", "coins[]", "1", "target", "COUNT", "518", "Add instead of max"],
        ["Coin Change II", "coins[]", "1", "target", "MIN", "322", "Init with INF"],
        ["Integer Break", "[1..n-1]", "product", "n", "MAX", "343", "Multiply not add"],
        ["Perfect Sq.", "[1,4,9..]", "1", "n", "MIN", "279", "Coins = squares"],
        ["Min Cost Tix", "[1,7,30]", "costs", "maxday", "MIN", "983", "Skip non-travel"],
        ["Word Break", "words", "bool", "len(s)", "OR", "139", "Substring match"],
        ["Word Break Cnt", "words", "1", "len(s)", "COUNT", "IK", "dp[i] += dp[j]"],
        ["Combo Sum IV", "nums[]", "1", "target", "COUNT", "377", "Swap loops!"],
    ]
    for row in data:
        pdf.table_row(row, w)

    pdf.trick_box("Combinations vs Permutations (swap the loops!)",
                  "Combinations (order doesn't matter): items outer, target inner\n"
                  "Permutations (order matters):        target outer, items inner\n\n"
                  "Coin Change Count = combinations (items outer)\n"
                  "Combination Sum IV = permutations (target outer)")

    pdf.section_title("Universal 1D Template (covers 90% of problems)")
    pdf.code_block("""def solve(items, target):
    dp = [BASE] * (target + 1)    # INF for MIN, 0 for MAX, 0 for COUNT
    dp[0] = INIT                  # 0 for MIN/MAX, 1 for COUNT

    for item in items:                          # outer: items
        for j in range(item, target + 1):       # inner: LEFT to RIGHT
            dp[j] = OP(dp[j], COMBINE(dp[j - item]))

    return dp[target]""")

    # =========================================================================
    # CHAPTER 4: LCS FAMILY
    # =========================================================================
    pdf.chapter_title("Chapter 4: LCS (Longest Common Subsequence) Family",
                      "16 problems - the MOTHER of all string DP")

    pdf.section_title("Identification: How to spot LCS problems")
    pdf.keyword_box([
        'TWO strings (or string vs its reverse) --> LCS family',
        '"subsequence" --> LCS (order matters, not contiguous)',
        '"substring" --> LCS with RESET on mismatch',
        '"palindrome" --> LCS(s, reverse(s))',
        '"convert A to B" --> LCS to find common, rest = operations',
    ])

    pdf.section_title("The Choice Diagram")
    pdf.code_block("""    Compare X[i-1] vs Y[j-1]:

    MATCH (X[i-1] == Y[j-1]):     1 + dp[i-1][j-1]   (both move back)
    
    NO MATCH:
      Subsequence: max(dp[i-1][j], dp[i][j-1])        (skip from X or Y)
      Substring:   0                                    (RESET! contiguous)""")

    pdf.section_title("LCS vs Knapsack Comparison")
    w = [45, 50, 50]
    pdf.table_row(["Aspect", "0/1 Knapsack", "LCS"], w, header=True)
    pdf.table_row(["What changes?", "items (n), capacity", "index i, index j"], w)
    pdf.table_row(["Choice", "pick or skip item", "match or skip char"], w)
    pdf.table_row(["On match/pick", "val + dp[i-1][w-wt]", "1 + dp[i-1][j-1]"], w)
    pdf.table_row(["On mismatch", "dp[i-1][w]", "max(dp[i-1][j],dp[i][j-1])"], w)
    pdf.table_row(["Base case", "dp[0][w] = 0", "dp[0][j] = dp[i][0] = 0"], w)

    pdf.section_title("All 16 Problems - Master Conversion Table")
    w = [55, 60, 25]
    pdf.table_row(["Problem", "Formula using LCS", "LC #"], w, header=True)
    pdf.table_row(["LCS length", "dp[m][n]", "1143"], w)
    pdf.table_row(["Longest Common Substring", "max dp[i][j] (reset on mismatch)", "-"], w)
    pdf.table_row(["Print LCS", "backtrack through dp table", "-"], w)
    pdf.table_row(["SCS length", "m + n - LCS(X, Y)", "-"], w)
    pdf.table_row(["Print SCS", "backtrack, add non-LCS chars", "-"], w)
    pdf.table_row(["Min Insert + Delete A->B", "(m - LCS) + (n - LCS)", "-"], w)
    pdf.table_row(["Longest Repeating Subseq", "LCS(s, s) with i != j", "-"], w)
    pdf.table_row(["Is A subseq of B?", "LCS(A,B) == len(A)", "392"], w)
    pdf.table_row(["Count subsequences", "dp + on match, carry on mismatch", "115"], w)
    pdf.table_row(["Longest Palindrome Subseq", "LCS(s, reverse(s))", "516"], w)
    pdf.table_row(["Min del for palindrome", "n - LCS(s, reverse(s))", "-"], w)
    pdf.table_row(["Min ins for palindrome", "n - LCS(s, reverse(s))", "-"], w)
    pdf.table_row(["Longest Palindrome Substr", "expand around center O(n^2)", "5"], w)
    pdf.table_row(["Count Palindrome Substrs", "expand around center O(n^2)", "647"], w)
    pdf.table_row(["Edit Distance", "1 + min(insert, delete, replace)", "72"], w)
    pdf.table_row(["Interleaving Strings", "dp[i][j] = OR(from s1, from s2)", "97"], w)

    pdf.section_title("Edit Distance (Levenshtein) - Key Formulas")
    pdf.code_block("""MATCH:     dp[i][j] = dp[i-1][j-1]           # FREE! no operation needed
NO MATCH:  dp[i][j] = 1 + min(
               dp[i][j-1],                     # INSERT  (add char to word1)
               dp[i-1][j],                     # DELETE  (remove from word1)
               dp[i-1][j-1]                    # REPLACE (swap char)
           )
BASE:      dp[i][0] = i,  dp[0][j] = j        # delete/insert all chars""")

    pdf.trick_box("Edit Distance vs LCS",
                  "If only INSERT and DELETE allowed (no REPLACE):\n"
                  "edit_distance = m + n - 2 * LCS(word1, word2)\n"
                  "This reduces to the min-insertions-deletions problem!")

    pdf.section_title("5-Finger Trick for LCS Revision")
    pdf.keyword_box([
        'THUMB:  "MATCH = diagonal (i-1,j-1) + 1"',
        'INDEX:  "MISMATCH = max(up, left) for SUBSEQ, 0 for SUBSTR"',
        'MIDDLE: "Palindrome = LCS(s, reverse(s))"',
        'RING:   "SCS = m + n - LCS"',
        'PINKY:  "Min ops = (m - LCS) + (n - LCS)"',
    ])

    # =========================================================================
    # CHAPTER 5: MCM / PARTITION DP
    # =========================================================================
    pdf.chapter_title("Chapter 5: MCM / Partition DP Family",
                      "8 problems - split range [i,j] at every k")

    pdf.section_title("Identification: How to spot MCM pattern")
    pdf.keyword_box([
        'Is there a STRING or ARRAY? --> YES',
        'Do I need to SPLIT/PARTITION it at every possible k? --> YES',
        'Does left part + right part give me the answer? --> YES = MCM!',
        '"partition", "split", "break", "merge" --> MCM pattern',
        '"parenthesize", "range [i,j]" --> MCM pattern',
    ])

    pdf.section_title("The Universal MCM Template (memorize this!)")
    pdf.code_block("""def solve(arr, i, j):
    # Step 1: BASE CASE
    if i >= j:
        return 0

    # Step 2: INITIALIZE
    ans = float('inf')   # or float('-inf') for MAX problems

    # Step 3: TRY ALL PARTITIONS
    for k in range(i, j):
        # Step 4: LEFT + RIGHT + MERGE COST
        temp = solve(arr, i, k) + solve(arr, k+1, j) + cost(i, k, j)
        # Step 5: OPTIMIZE
        ans = min(ans, temp)    # or max, or +=

    return ans""")

    pdf.section_title("Bottom-Up: DIAGONAL Filling (NOT row-by-row!)")
    pdf.trick_box("The KEY difference from Knapsack",
                  "Knapsack fills ROW by ROW (item by item)\n"
                  "MCM fills DIAGONALLY by GAP SIZE!\n\n"
                  "for gap in range(1, n):         # outer: gap size\n"
                  "    for i in range(n - gap):     # inner: start index\n"
                  "        j = i + gap\n"
                  "        dp[i][j] = ...           # fill using smaller gaps")

    pdf.section_title("All 8 MCM Problems - Master Table")
    w = [30, 25, 25, 35, 20, 15]
    pdf.table_row(["Problem", "Base Case", "k Range", "Cost Formula", "Optimize", "LC #"], w, header=True)
    pdf.table_row(["MCM", "i>=j -> 0", "i to j-1", "a[i-1]*a[k]*a[j]", "MIN", "-"], w)
    pdf.table_row(["Palindrome P.", "isPalin->0", "i to j-1", "1 per cut", "MIN", "132"], w)
    pdf.table_row(["Boolean Par.", "i==j->T/F", "operators", "truth table", "COUNT", "GFG"], w)
    pdf.table_row(["Scramble Str", "s1==s2->T", "1 to n-1", "swap/no-swap", "OR", "87"], w)
    pdf.table_row(["Egg Drop", "e=1->f", "1 to f", "1+max(b,s)", "MIN", "887"], w)
    pdf.table_row(["Burst Balloon", "i>j -> 0", "i to j", "a[i-1]*a[k]*a[j+1]", "MAX", "312"], w)
    pdf.table_row(["Merge Stones", "i==j->0", "step K-1", "rangeSum", "MIN", "1000"], w)
    pdf.table_row(["Polygon Tri.", "j-i<2->0", "i+1 to j-1", "v[i]*v[k]*v[j]", "MIN", "1039"], w)

    pdf.section_title("Burst Balloons - The Hardest Trick")
    pdf.trick_box("Think LAST to burst, NOT FIRST!",
                  "If we think 'burst first' --> neighbors keep changing --> impossible!\n"
                  "If we think 'burst LAST in range [i,j]' --> neighbors are fixed: i-1 and j+1\n\n"
                  "Add dummy 1s: nums = [1] + nums + [1]\n"
                  "Cost of bursting k LAST: nums[i-1] * nums[k] * nums[j+1]")

    pdf.section_title("Egg Dropping - 4 Levels of Optimization")
    pdf.keyword_box([
        'Level 1: Recursion O(2^f) -- try every floor k',
        'Level 2: Memoization O(e*f^2) -- cache (eggs, floors)',
        'Level 3: Memo + Binary Search O(e*f*log f) -- crossover point',
        'Level 4: Inverted DP O(e*log f) -- "given trials, find max floors"',
        'TRICK: break_cost increases, survive_cost decreases as k goes up',
    ])

    pdf.section_title("Boolean Parenthesization - Operator Truth Tables")
    pdf.code_block("""AND (&):  TrueWays  = LT * RT
          FalseWays = LF*RF + LF*RT + LT*RF

OR  (|):  TrueWays  = LT*RT + LT*RF + LF*RT
          FalseWays = LF * RF

XOR (^):  TrueWays  = LT*RF + LF*RT
          FalseWays = LT*RT + LF*RF

Memory:  AND = both true,  OR = at least one true,  XOR = exactly one true""")

    # =========================================================================
    # CHAPTER 6: STANDALONE DP
    # =========================================================================
    pdf.chapter_title("Chapter 6: Standalone DP Problems",
                      "Important problems that don't fit the big 3 families")

    pdf.problem_header("1", "Count Ways to Reach Nth Step (Climbing Stairs)", "Easy", "Amazon, Google, Microsoft, Meta, Apple")
    pdf.formula_box("dp[i] = dp[i-1] + dp[i-2]   (Fibonacci!)")
    pdf.body_text("Base: dp[0]=1, dp[1]=1. Space O(1): only need prev 2 values.")
    pdf.trick_box("Generalization",
                  "If steps allowed = {1,2,3}: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]\n"
                  "If steps from set S: dp[i] = sum(dp[i-s] for s in S) = Coin Change!")

    pdf.problem_header("2", "Jump Game", "Medium", "Amazon, Google, Microsoft, Meta")
    pdf.body_text("Given nums[i] = max jump from position i, can you reach the end?")
    pdf.formula_box("Greedy: track farthest reachable. If i > farthest --> stuck!")
    pdf.code_block("""def jump_game(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest: return False
        farthest = max(farthest, i + nums[i])
    return True""")
    pdf.trick_box("DP exists but Greedy is O(n) optimal",
                  "DP approach: dp[i] = can reach index i? O(n^2)\n"
                  "Greedy: track farthest position O(n) -- ALWAYS present this!")

    pdf.problem_header("3", "Robbery / House Robber", "Medium", "Amazon, Google, Microsoft, Meta, Goldman Sachs")
    pdf.body_text("Max money robbing non-adjacent houses.")
    pdf.formula_box("dp[i] = max(nums[i] + dp[i-2],  dp[i-1])")
    pdf.body_text("        (rob this + skip prev)  (skip this)")
    pdf.code_block("""def rob(nums):
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(num + prev2, prev1)
    return prev1""")
    pdf.trick_box("Follow-ups",
                  "House Robber II (circle): run twice on [0..n-2] and [1..n-1], take max\n"
                  "House Robber III (tree): DFS returning (rob, skip) pair per node")

    pdf.problem_header("4", "Knight's Tour on Phone Keypad", "Medium", "Google, Amazon, Microsoft")
    pdf.body_text("Count distinct phone numbers of length n using knight moves on keypad.")
    pdf.code_block("""Jump Map (memorize!):
0->[4,6]  1->[6,8]  2->[7,9]  3->[4,8]  4->[0,3,9]
5->[]     6->[0,1,7] 7->[2,6] 8->[1,3]  9->[2,4]

dp[digit] = sum(dp[prev] for prev in moves[digit])
Only 10 states --> O(1) space with rolling array!""")

    pdf.problem_header("5", "Largest Square Submatrix With All 1s", "Medium", "Amazon, Google, Microsoft, Goldman Sachs")
    pdf.formula_box("dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])  if cell='1'")
    pdf.body_text("The MIN is the bottleneck! A square needs all 3 neighbors to be large enough.")
    pdf.trick_box("Return AREA not side!", "Answer = max_side * max_side")

    pdf.problem_header("6", "Word Wrap", "Medium-Hard", "Google, Amazon, Microsoft")
    pdf.body_text("Arrange words on lines to minimize cost of extra spaces.")
    pdf.formula_box("dp[i] = min(cost(i,j) + dp[j+1])  for all valid j where words i..j fit")
    pdf.trick_box("Key details",
                  "Cost = (extra_spaces)^3 (or ^2, ask interviewer!)\n"
                  "Last line cost = 0 (no penalty for trailing spaces)\n"
                  "Greedy packing is NOT optimal -- that's why we need DP!")

    # =========================================================================
    # CHAPTER 7: ULTIMATE CHEAT SHEET
    # =========================================================================
    pdf.chapter_title("Chapter 7: Ultimate Cheat Sheet",
                      "Everything on quick-reference pages - your last-minute revision")

    pdf.section_title("Pattern Recognition - See This? Think That!")
    w = [85, 55]
    pdf.table_row(["You See This...", "Think This!"], w, header=True)
    pdf.table_row(["Pick or skip + capacity/sum", "0/1 Knapsack"], w)
    pdf.table_row(["Infinite supply / reuse items", "Unbounded Knapsack"], w)
    pdf.table_row(["Two strings, what's common?", "LCS"], w)
    pdf.table_row(["String vs its reverse", "LCS -> Palindrome"], w)
    pdf.table_row(["Convert string A to B", "Edit Distance (LCS variant)"], w)
    pdf.table_row(["Split/partition a range", "MCM"], w)
    pdf.table_row(["Can't pick adjacent elements", "House Robber"], w)
    pdf.table_row(["Count ways with 1/2 steps", "Fibonacci DP"], w)
    pdf.table_row(["Largest square in matrix", "Matrix DP: min(top,left,diag)+1"], w)
    pdf.table_row(["Min trials worst case", "Egg Drop (MCM variant)"], w)
    pdf.table_row(["Boolean expression ways", "Boolean Parenthesization (MCM)"], w)
    pdf.table_row(["Burst/merge elements", "Burst Balloons (MCM, think LAST)"], w)

    pdf.section_title("Formula Cheat Sheet (memorize these!)")
    formulas = [
        "LCS length            = dp[m][n]",
        "Longest Palindrome     = LCS(s, reverse(s))",
        "SCS length             = m + n - LCS",
        "Min del for palindrome = n - LCS(s, reverse(s))",
        "Min insert + delete    = (m - LCS) + (n - LCS)",
        "Edit Distance          = 1 + min(insert, delete, replace)",
        "Equal Partition        = Subset Sum with target = totalSum / 2",
        "Target Sum             = Count Subsets with sum = (total + target) / 2",
        "Min Subset Diff        = total - 2 * (best S1 <= total/2)",
    ]
    for f in formulas:
        pdf.formula_box(f)

    pdf.section_title("Complexity Summary - All Families")
    w = [35, 25, 25, 30, 30]
    pdf.table_row(["Family", "Recursion", "Memo/BU", "Space Opt", "Key"], w, header=True)
    pdf.table_row(["0/1 Knapsack", "O(2^n)", "O(n*W)", "O(W) 1D", "Right to Left"], w)
    pdf.table_row(["Unbounded KS", "O(2^n)", "O(n*W)", "O(W) 1D", "Left to Right"], w)
    pdf.table_row(["LCS", "O(2^(m+n))", "O(m*n)", "O(min(m,n))", "2 rows"], w)
    pdf.table_row(["MCM", "O(2^n)", "O(n^3)", "O(n^2)", "Diagonal fill"], w)
    pdf.table_row(["Edit Distance", "O(3^(m+n))", "O(m*n)", "O(n)", "2 rows"], w)
    pdf.table_row(["Egg Drop", "O(2^f)", "O(e*f^2)", "O(e)", "Inverted DP"], w)

    pdf.section_title("The 3-Line Memo Conversion (works EVERYWHERE)")
    pdf.code_block("""# 1. Create:   memo = {}   (or 2D array [-1])
# 2. Check:    if key in memo: return memo[key]
# 3. Store:    memo[key] = result; return memo[key]""")

    pdf.section_title("Key Differences to Never Confuse")
    w = [48, 48, 48]
    pdf.table_row(["Aspect", "0/1 Knapsack", "Unbounded"], w, header=True)
    pdf.table_row(["Item reuse", "At most ONCE", "UNLIMITED"], w)
    pdf.table_row(["2D: include row", "dp[i-1][...]", "dp[i][...]"], w)
    pdf.table_row(["1D: loop direction", "RIGHT to LEFT", "LEFT to RIGHT"], w)
    pdf.table_row(["Keyword", "'each item once'", "'infinite supply'"], w)

    pdf.ln(5)
    w = [48, 48, 48]
    pdf.table_row(["Aspect", "Knapsack (row)", "MCM (diagonal)"], w, header=True)
    pdf.table_row(["Fill order", "Row by row", "Gap by gap"], w)
    pdf.table_row(["Depends on", "Previous row only", "Many smaller ranges"], w)
    pdf.table_row(["Space reduce?", "YES: 1D array", "NO: need full 2D"], w)
    pdf.table_row(["Typical time", "O(n*W)", "O(n^3)"], w)

    pdf.section_title("Interview Flow (follow this EVERY time)")
    pdf.keyword_box([
        '1. READ problem --> identify pattern (Knapsack? LCS? MCM? Other?)',
        '2. DRAW choice diagram on whiteboard',
        '3. WRITE recursion with base case',
        '4. CONVERT to memoization (add 3 lines)',
        '5. OFFER bottom-up if asked (show you know both)',
        '6. OPTIMIZE space if asked (1D array trick)',
        '7. STATE complexity: Time O(?), Space O(?)',
    ])

    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(25, 25, 112)
    pdf.cell(0, 10, "You've got this! Go crush those FAANG interviews!", align="C")

    # =========================================================================
    # CHAPTER 8: VISUAL DIAGRAMS
    # =========================================================================
    pdf.chapter_title("Chapter 8: Visual Architecture Diagrams",
                      "Complete visual maps of all DP families, relationships, and conversion flows")

    pdf.draw_family_overview_diagram()
    pdf.draw_standalone_diagram()
    pdf.draw_approach_flow_diagram()
    pdf.draw_knapsack_vs_unbounded_diagram()
    pdf.draw_mcm_diagonal_diagram()

    # =========================================================================
    # SAVE
    # =========================================================================
    out_path = os.path.join(
        r"e:\Sheriff_faang\FaangCompanyPreprations\Faang_Preparations",
        "DP_FAANG_Revision_Guide.pdf"
    )
    pdf.output(out_path)
    print(f"PDF saved to: {out_path}")
    return out_path


if __name__ == "__main__":
    build_pdf()
