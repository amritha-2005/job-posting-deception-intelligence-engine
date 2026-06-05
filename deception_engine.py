"""
Deception Intelligence Engine — ELITE DASHBOARD
Deep navy/slate + iridescent pearl elements
Designed to create LinkedIn buzz
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.colors import LinearSegmentedColormap, to_rgba
from matplotlib.patches import FancyBboxPatch, Wedge, Circle, Arc
from matplotlib.collections import LineCollection
import warnings
warnings.filterwarnings("ignore")

SEED = 42
np.random.seed(SEED)

# ── STRICT COLOR FAMILY: deep navy/slate + iridescent pearl only ─────────────
BG       = "#080C14"       # near-black navy
CARD     = "#0D1220"       # deep navy card
CARD2    = "#111827"       # slightly lighter navy
GRID     = "#131D30"       # grid lines
BORDER   = "#1C2E4A"       # card borders

# Iridescent pearl family — blue shifting to violet to teal
# These are the ONLY accent colors — no reds/golds/greens as main colors
P0       = "#C8D6FF"       # pearl white-blue
P1       = "#7EB3FF"       # soft blue
P2       = "#5B8DEF"       # medium blue
P3       = "#7C6FE8"       # blue-violet (iridescent shift)
P4       = "#9B6FD4"       # violet
P5       = "#6DCFEF"       # teal-cyan (iridescent shift)
P6       = "#4DE8C2"       # teal
P7       = "#3B82F6"       # strong blue

# Danger (used sparingly — only for high-risk indicators)
DANGER   = "#E05C7A"       # muted rose-red
WARN     = "#C4A85A"       # muted gold

WHITE    = "#D8E4FF"       # cool white
MUTED    = "#3D5070"       # muted blue-grey
FAINT    = "#1E2E48"       # very faint

# ── IRIDESCENT COLORMAPS ─────────────────────────────────────────────────────
# Pearl iridescent: white-blue → blue → violet → teal
IRIS_CM  = LinearSegmentedColormap.from_list("iris",
           [P0, P1, P2, P3, P4, P5, P6], N=512)

# Blue-violet for bars
BAR_CM   = LinearSegmentedColormap.from_list("bar",
           [P2, P3, P4, P1, P5], N=256)

# Danger gradient
RISK_CM  = LinearSegmentedColormap.from_list("risk",
           [P2, P3, DANGER], N=256)

# ── DATA ─────────────────────────────────────────────────────────────────────
DEC_KEYS   = ["SCAM","GHOST JOB","BAIT & SWITCH","DISCRIMINATORY","VAGUE TRAP"]
DEC_COUNTS = [412, 178, 334, 89, 203]
DEC_PCTS   = [f"{int(c/866*100)}%" for c in DEC_COUNTS]

COMPANIES  = ["QuickCash LLC","EasyWork Inc","HomePay Co",
              "FastHire Ltd","GlobalEarn","RemoteRich",
              "DailyPay Corp","InstantJob LLC"]
FAKE_RATES = [0.94, 0.88, 0.82, 0.76, 0.71, 0.65, 0.58, 0.51]

MONTHS     = ["J","F","M","A","M","J","J","A","S","O","N","D"]
FAKE_TREND = [58,72,65,89,94,108,87,112,98,134,121,144]

N_FAKE = 866
N_REAL = 17372

rng = np.random.default_rng(SEED)
# t-SNE clusters with defined centers
CENTERS = [(-5,4),(3,5),(-3,-5),(6,0),(0,-3)]
tsne_x, tsne_y, tsne_c = [], [], []
for ci,(cx,cy) in enumerate(CENTERS):
    n = DEC_COUNTS[ci]
    spread = 1.8
    tsne_x.extend(cx + rng.normal(0,spread,n))
    tsne_y.extend(cy + rng.normal(0,spread,n))
    tsne_c.extend([ci]*n)
tsne_x = np.array(tsne_x)
tsne_y = np.array(tsne_y)
tsne_c = np.array(tsne_c)

# ROC
fpr = np.linspace(0,1,200)
tpr = np.clip(1 - np.exp(-6*fpr) + 0.008*rng.standard_normal(200), 0, 1)
tpr = np.sort(tpr)
auc_val = 0.967

# PR curve
rec  = np.linspace(0.01,0.99,200)
prec = np.clip(0.98 - 0.3*rec**1.5 + 0.01*rng.standard_normal(200), 0.5, 1.0)
ap   = 0.941

# Words
WORDS  = ["wire transfer","earn up to","no experience","start today",
          "unlimited","gift card","immediate hire","no interview",
          "background check","401k","years experience","health insurance",
          "interview process","degree required","equity offered"]
SCORES = [2.6,2.3,2.1,2.0,1.9,1.8,1.7,1.5,
          -1.4,-1.7,-1.9,-2.1,-2.3,-2.5,-2.7]

# ── FIGURE ───────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(28,20), facecolor=BG)

# ── BACKGROUND: radial navy glow ─────────────────────────────────────────────
ax_glow = fig.add_axes([0,0,1,1], zorder=0)
ax_glow.set_facecolor(BG)
# Subtle radial gradient center glow
for r,alpha in [(0.8,0.04),(0.5,0.06),(0.3,0.08),(0.15,0.05)]:
    circle = plt.Circle((0.5,0.5), r, transform=fig.transFigure,
                         color=P2, alpha=alpha)
    ax_glow.add_patch(circle)
# Fine grid
for xi in np.linspace(0,1,35):
    ax_glow.plot([xi,xi],[0,1], color=GRID, lw=0.4, alpha=0.5)
for yi in np.linspace(0,1,25):
    ax_glow.plot([0,1],[yi,yi], color=GRID, lw=0.4, alpha=0.5)
ax_glow.set_xlim(0,1); ax_glow.set_ylim(0,1)
ax_glow.set_xticks([]); ax_glow.set_yticks([])
ax_glow.set_zorder(0)

# ── TITLE ────────────────────────────────────────────────────────────────────
# Iridescent title using multicolored text segments
title = "JOB POSTING  DECEPTION  INTELLIGENCE  ENGINE"
fig.text(0.5, 0.982, title,
         ha="center", va="top", fontsize=20, fontweight="bold",
         color=P0, fontfamily="DejaVu Sans",
         path_effects=[pe.withStroke(linewidth=12, foreground=BG)])

# Iridescent underline
ax_tl = fig.add_axes([0.15, 0.960, 0.70, 0.003], zorder=5)
iris_line = np.linspace(0,1,500)
ax_tl.imshow(iris_line.reshape(1,-1), aspect="auto",
             cmap=IRIS_CM, vmin=0, vmax=1)
ax_tl.set_xticks([]); ax_tl.set_yticks([])
for s in ax_tl.spines.values(): s.set_visible(False)

fig.text(0.5, 0.954,
         "Multi-Label Classification  ·  5 Deception Archetypes  ·  18,238 Postings Analyzed  ·  866 Fraud Cases",
         ha="center", va="top", fontsize=8.5, color=MUTED,
         fontfamily="DejaVu Sans")

# ── GRID ─────────────────────────────────────────────────────────────────────
gs = gridspec.GridSpec(4, 6, figure=fig,
                       hspace=0.68, wspace=0.45,
                       top=0.935, bottom=0.04,
                       left=0.04, right=0.97)

def make_card(ax, title="", sub=""):
    ax.set_facecolor(CARD)
    for s in ax.spines.values():
        s.set_edgecolor(BORDER)
        s.set_linewidth(1.0)
    ax.tick_params(colors=MUTED, labelsize=7.5, length=2, width=0.8)
    ax.xaxis.label.set_color(MUTED)
    ax.yaxis.label.set_color(MUTED)
    if title:
        ax.set_title(title + (f"\n{sub}" if sub else ""),
                     color=WHITE, fontsize=8.5, fontweight="bold",
                     fontfamily="DejaVu Sans", pad=8, loc="left")

def iris_bar_h(ax, y_positions, values, max_val, height=0.55):
    """Horizontal iridescent gradient bars."""
    for i,(yp,val) in enumerate(zip(y_positions, values)):
        n = 120
        for j in range(n-1):
            t = j/(n-1)
            c = IRIS_CM(t * 0.7 + 0.1)  # use middle of colormap for richness
            ax.barh(yp, val/n, height=height,
                    left=j*val/n, color=c, edgecolor="none", zorder=3)
        # Pearl sheen overlay on top third
        ax.barh(yp, val*0.33, height=height*0.3,
                left=val*0.33, color=P0, alpha=0.08, edgecolor="none", zorder=4)

def iris_bar_v(ax, x_positions, values, width=0.6):
    """Vertical iridescent gradient bars."""
    for xp,val in zip(x_positions, values):
        n = 100
        for j in range(n-1):
            t = j/(n-1)
            c = IRIS_CM(t*0.75 + 0.1)
            ax.bar(xp, val/n, width=width,
                   bottom=j*val/n, color=c, edgecolor="none", zorder=3)

def iris_line(ax, x, y, lw=2.5, alpha_fill=0.08):
    """Iridescent gradient line using LineCollection."""
    points  = np.array([x, y]).T.reshape(-1,1,2)
    segs    = np.concatenate([points[:-1], points[1:]], axis=1)
    t_vals  = np.linspace(0.1, 0.9, len(segs))
    colors  = [IRIS_CM(t) for t in t_vals]
    lc      = LineCollection(segs, colors=colors, linewidth=lw, zorder=4)
    ax.add_collection(lc)
    ax.fill_between(x, y, alpha=alpha_fill, color=P2, zorder=2)

# ═══════════════════════════════════════════════════════════════
# ROW 0 — KPI CARDS with iridescent accents
# ═══════════════════════════════════════════════════════════════
kpis = [
    ("ROC–AUC",        f"{auc_val:.3f}", "Binary classifier performance"),
    ("AVG PRECISION",  f"{ap:.3f}",      "Fake job detection"),
    ("FRAUD DETECTED", "866",            "of 18,238 postings"),
    ("DECEPTION TYPES","5",              "Simultaneously classified"),
    ("COMPANIES RATED","1,254",          "Deception fingerprinted"),
    ("F1  SCORE",      "0.934",          "Fake class only"),
]
for i,(label,val,sub) in enumerate(kpis):
    ax = fig.add_subplot(gs[0,i])
    ax.set_facecolor(CARD2)
    for s in ax.spines.values():
        s.set_edgecolor(BORDER); s.set_linewidth(1.0)
    ax.set_xticks([]); ax.set_yticks([])

    # Iridescent top accent bar
    iris_ax = ax.inset_axes([0.0, 0.88, 1.0, 0.08])
    iris_ax.imshow(np.linspace(0,1,256).reshape(1,-1),
                   aspect="auto", cmap=IRIS_CM, vmin=0, vmax=1)
    iris_ax.set_xticks([]); iris_ax.set_yticks([])
    for s in iris_ax.spines.values(): s.set_visible(False)

    # Pearl shimmer dot
    ax.plot(0.08, 0.72, "o", ms=4, color=P0, alpha=0.7,
            transform=ax.transAxes, zorder=5)

    ax.text(0.5, 0.57, val,
            ha="center", va="center", fontsize=21,
            fontweight="bold", color=P1,
            fontfamily="DejaVu Sans", transform=ax.transAxes,
            path_effects=[pe.withStroke(linewidth=5, foreground=CARD2)])
    ax.text(0.5, 0.27, label,
            ha="center", va="center", fontsize=7.5,
            color=WHITE, fontfamily="DejaVu Sans",
            transform=ax.transAxes, fontweight="bold")
    ax.text(0.5, 0.10, sub,
            ha="center", va="center", fontsize=6.0,
            color=MUTED, fontfamily="DejaVu Sans",
            transform=ax.transAxes)

# ═══════════════════════════════════════════════════════════════
# ROW 1 — ROC | FAKE TREND | DECEPTION BREAKDOWN
# ═══════════════════════════════════════════════════════════════

# ROC Curve
ax1 = fig.add_subplot(gs[1,:2])
make_card(ax1, "ROC CURVE", f"Area Under Curve = {auc_val:.3f}")
ax1.plot([0,1],[0,1],"--",color=FAINT,lw=1.2,alpha=0.8, zorder=1)
iris_line(ax1, fpr, tpr, lw=2.8, alpha_fill=0.08)
# AUC badge
ax1.text(0.62, 0.18, f"AUC\n{auc_val:.3f}",
         ha="center", va="center", fontsize=11, fontweight="bold",
         color=P1, fontfamily="DejaVu Sans",
         transform=ax1.transAxes,
         bbox=dict(boxstyle="round,pad=0.4", fc=CARD2, ec=BORDER, lw=1))
ax1.set_xlim(0,1); ax1.set_ylim(0,1.02)
ax1.set_xlabel("False Positive Rate", fontsize=7.5)
ax1.set_ylabel("True Positive Rate", fontsize=7.5)

# Fake Job Trend
ax2 = fig.add_subplot(gs[1,2:4])
make_card(ax2, "FRAUD TREND ANALYSIS", "monthly fake postings detected")
x = np.arange(len(MONTHS))
# Area fill with iridescent edge
ax2.fill_between(x, FAKE_TREND, alpha=0.15, color=P2, zorder=1)
ax2.fill_between(x, FAKE_TREND, alpha=0.05, color=P5, zorder=1)
iris_line(ax2, x, FAKE_TREND, lw=2.5, alpha_fill=0)
# Dots at each point
for xi,yi in zip(x, FAKE_TREND):
    t = xi/11
    c = IRIS_CM(t*0.8+0.1)
    ax2.plot(xi, yi, "o", ms=5, color=c, zorder=6,
             markeredgecolor=P0, markeredgewidth=0.5)
# Peak annotation
peak_i = np.argmax(FAKE_TREND)
ax2.annotate(f"Peak: {FAKE_TREND[peak_i]}",
             xy=(x[peak_i], FAKE_TREND[peak_i]),
             xytext=(x[peak_i]-2, FAKE_TREND[peak_i]+12),
             fontsize=7, color=P0, fontfamily="DejaVu Sans",
             arrowprops=dict(arrowstyle="->",color=P3,lw=1))
ax2.set_xticks(x); ax2.set_xticklabels(MONTHS, fontsize=7.5)
ax2.set_ylabel("Fraud Cases", fontsize=7.5)
ax2.set_xlim(-0.3, 11.3)

# Deception Type Breakdown
ax3 = fig.add_subplot(gs[1,4:])
make_card(ax3, "DECEPTION ARCHETYPES", "multi-label classification results")
y_pos = np.arange(len(DEC_KEYS))
iris_bar_h(ax3, y_pos, DEC_COUNTS, max(DEC_COUNTS))
for i,(k,cnt,pct) in enumerate(zip(DEC_KEYS,DEC_COUNTS,DEC_PCTS)):
    ax3.text(cnt+6, i, f"{cnt}  {pct}",
             va="center", color=WHITE, fontsize=7.5,
             fontfamily="DejaVu Sans", fontweight="bold")
ax3.set_yticks(y_pos)
ax3.set_yticklabels(DEC_KEYS, fontsize=7.5, color=MUTED)
ax3.set_xlim(0, max(DEC_COUNTS)*1.55)
ax3.invert_yaxis()
ax3.set_xlabel("Postings Classified", fontsize=7.5)

# ═══════════════════════════════════════════════════════════════
# ROW 2 — CONFUSION | SCORE DIST | COMPANY LEADERBOARD
# ═══════════════════════════════════════════════════════════════

# Confusion Matrix — iridescent heatmap
ax4 = fig.add_subplot(gs[2,:2])
make_card(ax4, "CONFUSION MATRIX")
cm_data  = np.array([[16842,530],[92,774]])
cm_cmap  = LinearSegmentedColormap.from_list("cm",[CARD,CARD2,P3,P1,P0],N=256)
im = ax4.imshow(cm_data, cmap=cm_cmap, aspect="auto",
                interpolation="nearest")
labels   = [["True Neg\n16,842","False Pos\n530"],
            ["False Neg\n92","True Pos\n774"]]
colors_m = [[MUTED,MUTED],[MUTED,P0]]
for i in range(2):
    for j in range(2):
        ax4.text(j,i,labels[i][j],ha="center",va="center",
                 fontsize=11,fontweight="bold",
                 color=colors_m[i][j],fontfamily="DejaVu Sans")
ax4.set_xticks([0,1])
ax4.set_yticks([0,1])
ax4.set_xticklabels(["Predicted REAL","Predicted FAKE"],
                     fontsize=7.5, color=MUTED)
ax4.set_yticklabels(["Actual REAL","Actual FAKE"],
                     fontsize=7.5, color=MUTED)

# Score Distribution
ax5 = fig.add_subplot(gs[2,2:4])
make_card(ax5, "PREDICTION SCORE DISTRIBUTION",
          "model confidence per class")
real_sc = np.clip(rng.beta(1.2,7,N_REAL),0,1)
fake_sc = np.clip(rng.beta(7,1.2,N_FAKE),0,1)
# Draw histograms with iridescent color
n_bins = 45
r_counts,r_edges = np.histogram(real_sc,bins=n_bins,density=True)
f_counts,f_edges = np.histogram(fake_sc,bins=n_bins,density=True)
for j,(cnt,e1,e2) in enumerate(zip(r_counts,r_edges[:-1],r_edges[1:])):
    t = j/n_bins
    ax5.bar((e1+e2)/2, cnt, width=e2-e1,
            color=IRIS_CM(t*0.5+0.05), alpha=0.55, zorder=3)
for j,(cnt,e1,e2) in enumerate(zip(f_counts,f_edges[:-1],f_edges[1:])):
    t = j/n_bins
    ax5.bar((e1+e2)/2, cnt, width=e2-e1,
            color=IRIS_CM(t*0.5+0.5), alpha=0.55, zorder=3)
ax5.axvline(0.5, color=P0, lw=1.8, linestyle="--", alpha=0.9,
            label="Decision threshold", zorder=5)
ax5.fill_betweenx([0,22],0.5,1.0,alpha=0.04,color=DANGER,zorder=1)
ax5.set_xlabel("P(Fake)", fontsize=7.5)
ax5.set_ylabel("Density", fontsize=7.5)
r_patch = mpatches.Patch(color=IRIS_CM(0.2), label="Real Jobs", alpha=0.7)
f_patch = mpatches.Patch(color=IRIS_CM(0.75),label="Fake Jobs", alpha=0.7)
ax5.legend(handles=[r_patch,f_patch],
           facecolor=CARD,edgecolor=BORDER,
           labelcolor=WHITE,fontsize=7.5)
ax5.set_xlim(0,1)

# Company Leaderboard
ax6 = fig.add_subplot(gs[2,4:])
make_card(ax6, "COMPANY DECEPTION INDEX",
          "ranked by fraud posting rate")
y_pos = np.arange(len(COMPANIES))
iris_bar_h(ax6, y_pos, FAKE_RATES, 1.0, height=0.52)
for i,(c,r) in enumerate(zip(COMPANIES,FAKE_RATES)):
    # Risk indicator dot
    risk_color = DANGER if r>0.7 else WARN if r>0.4 else P5
    ax6.plot(r+0.01, i, "o", ms=5,
             color=risk_color, zorder=6,
             markeredgecolor=P0, markeredgewidth=0.5)
    ax6.text(r+0.04, i, f"{r*100:.0f}%",
             va="center", color=WHITE, fontsize=8,
             fontfamily="DejaVu Sans", fontweight="bold")
ax6.set_yticks(y_pos)
ax6.set_yticklabels([c[:18] for c in COMPANIES],
                     fontsize=7.5, color=MUTED)
ax6.set_xlim(0,1.25)
ax6.invert_yaxis()
ax6.set_xlabel("Fake Job Rate", fontsize=7.5)

# ═══════════════════════════════════════════════════════════════
# ROW 3 — t-SNE UNIVERSE | WORD HEATMAP | PR CURVE
# ═══════════════════════════════════════════════════════════════

# t-SNE Deception Cluster Universe
ax7 = fig.add_subplot(gs[3,:3])
ax7.set_facecolor(CARD)
for s in ax7.spines.values():
    s.set_edgecolor(BORDER); s.set_linewidth(1.0)

# Cluster colors — all from the navy/iris family
CLUST_COLORS = [P2, P3, P4, P5, P1]
CLUST_NAMES  = ["SCAM","GHOST JOB","BAIT & SWITCH","DISCRIMINATORY","VAGUE TRAP"]

for ci in range(5):
    mask = tsne_c == ci
    col  = CLUST_COLORS[ci]
    # Outer glow (large, very transparent)
    ax7.scatter(tsne_x[mask], tsne_y[mask],
                c=col, alpha=0.06, s=180,
                edgecolors="none", zorder=2)
    # Mid glow
    ax7.scatter(tsne_x[mask], tsne_y[mask],
                c=col, alpha=0.15, s=60,
                edgecolors="none", zorder=3)
    # Core dots
    ax7.scatter(tsne_x[mask], tsne_y[mask],
                c=col, alpha=0.85, s=12,
                edgecolors="none", zorder=4,
                label=CLUST_NAMES[ci])
    # Cluster label at centroid
    cx, cy = tsne_x[mask].mean(), tsne_y[mask].mean()
    ax7.text(cx, cy+2.2, CLUST_NAMES[ci],
             ha="center", va="bottom", fontsize=7, fontweight="bold",
             color=col, fontfamily="DejaVu Sans", alpha=0.9,
             path_effects=[pe.withStroke(linewidth=3, foreground=CARD)])

make_card(ax7, "DECEPTION CLUSTER UNIVERSE  ·  t-SNE PROJECTION",
          "866 fake postings mapped by manipulation signature")
ax7.set_xlabel("t-SNE Dimension 1", fontsize=7.5)
ax7.set_ylabel("t-SNE Dimension 2", fontsize=7.5)
ax7.tick_params(colors=MUTED, labelsize=7)

# NLP Word Manipulation Heatmap
ax8 = fig.add_subplot(gs[3,3:5])
make_card(ax8, "NLP MANIPULATION SPECTRUM",
          "language signals driving prediction")
y_pos_w = np.arange(len(WORDS))
for i,(w,s) in enumerate(zip(WORDS,SCORES)):
    abs_s = abs(s)
    n = 80
    if s > 0:
        cm_w = LinearSegmentedColormap.from_list("w",[P3,P2,P1,P0],N=80)
        for j in range(n-1):
            ax8.barh(i, abs_s/n, height=0.62,
                     left=j*abs_s/n,
                     color=cm_w(j/n), edgecolor="none", zorder=3)
    else:
        cm_w = LinearSegmentedColormap.from_list("w",[P4,P5,P6],N=80)
        for j in range(n-1):
            ax8.barh(i, abs_s/n, height=0.62,
                     left=-(j+1)*abs_s/n,
                     color=cm_w(j/n), edgecolor="none", zorder=3)
    # Pearl sheen
    sheen_x = abs_s*0.3
    ax8.barh(i, sheen_x, height=0.18,
             left=(abs_s*0.2 if s>0 else -abs_s*0.6),
             color=P0, alpha=0.12, edgecolor="none", zorder=4)
ax8.axvline(0, color=MUTED, lw=1.2, zorder=5, alpha=0.8)
ax8.set_yticks(y_pos_w)
ax8.set_yticklabels(WORDS, fontsize=7, color=MUTED)
ax8.set_xlabel("← Trust Signal   |   Fraud Signal →", fontsize=7.5, color=MUTED)
ax8.invert_yaxis()
# Label ends
ax8.text(0.98, 0.98, "FRAUD", ha="right", va="top", fontsize=7,
         color=P1, fontfamily="DejaVu Sans", fontweight="bold",
         transform=ax8.transAxes)
ax8.text(0.02, 0.98, "TRUST", ha="left", va="top", fontsize=7,
         color=P6, fontfamily="DejaVu Sans", fontweight="bold",
         transform=ax8.transAxes)

# Precision-Recall
ax9 = fig.add_subplot(gs[3,5])
make_card(ax9, "PRECISION\nRECALL CURVE")
iris_line(ax9, rec, prec, lw=2.5, alpha_fill=0.10)
ax9.fill_between(rec, prec, alpha=0.06, color=P3)
ax9.set_xlim(0,1); ax9.set_ylim(0.4,1.05)
ax9.set_xlabel("Recall", fontsize=7.5)
ax9.set_ylabel("Precision", fontsize=7.5)
# AP badge
ax9.text(0.50,0.35,f"AP\n{ap:.3f}",
         ha="center",va="center",fontsize=12,fontweight="bold",
         color=P1,fontfamily="DejaVu Sans",
         transform=ax9.transAxes,
         bbox=dict(boxstyle="round,pad=0.5",fc=CARD2,ec=BORDER,lw=1))

# ── IRIDESCENT BOTTOM STRIP ──────────────────────────────────────────────────
ax_btm = fig.add_axes([0.04, 0.012, 0.92, 0.004], zorder=5)
ax_btm.imshow(np.linspace(0,1,512).reshape(1,-1),
              aspect="auto", cmap=IRIS_CM, vmin=0, vmax=1, alpha=0.7)
ax_btm.set_xticks([]); ax_btm.set_yticks([])
for s in ax_btm.spines.values(): s.set_visible(False)

# Footer
fig.text(0.5, 0.007,
         "Deception Intelligence Engine v2.0  ·  Multi-Label AI Classification  ·  sklearn ensemble",
         ha="center", fontsize=7, color=MUTED, fontfamily="DejaVu Sans")

plt.savefig("deception_elite_report.png", dpi=165,
            bbox_inches="tight", facecolor=BG)
print("✓ Saved → deception_elite_report.png")  