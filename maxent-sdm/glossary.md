# Glossary — Species Distribution Modelling with Maxent

Terms as used in this course. The list follows the glossary in the supplement of Merow, Smith & Silander (2013),
*A practical guide to MaxEnt for modeling species' distributions*, Ecography 36: 1–12, written here in our own words
and tied to the Javan gibbon example.

**Accessible area (M).** The area a species could have reached, given its dispersal and history. The background
should be drawn from it. For our records: Banten and Jawa Barat (module M1).

**AUC (area under the ROC curve).** The chance that a random presence gets a higher prediction than a random
background cell. With presence-only data it compares presences with background, not with absences, so it depends on
the background and can be compared only between models built on the same background (M6).

**Background.** A random sample of cells from the study area (10,000 by default) that describes the conditions
available. Presence or absence is unknown there. Not the same as absence (M1, M4).

**Bias file.** A grid of relative sampling effort. Maxent then draws the background in proportion to it, so that the
background has the same sampling bias as the records (M8).

**Categorical variable.** A variable whose values are classes, not amounts, such as forest function. Maxent makes
one feature per class (M3).

**Clamping.** When a model is projected to conditions outside the training range, each variable is held at its
training minimum or maximum. The clamping grid shows where this changed the prediction (M10).

**Cloglog output.** Maxent's default output since version 3.4: values from 0 to 1, read as relative suitability.
It can be interpreted as a probability of presence only under an assumption about how common the species is (M4).

**Cross-validation.** Splitting the records into k groups and testing each group on a model fitted to the others.
Random folds of clustered records are optimistic; holding out whole sites (spatial blocks) is a stricter test (M6).

**Cumulative output.** Ranks cells from 0 to 100; a threshold at c leaves out about c % of the presences (M4).

**Entropy.** A measure of how spread out a distribution is. Maxent chooses the most spread-out distribution that
still matches the conditions at the records — it assumes nothing more than the data tell it (M4).

**Feature.** A transformation of an environmental variable: linear, quadratic, product, threshold, hinge, or one per
class for a categorical variable. A **hinge** is flat up to a knot and then a straight line (forward hinge) or a line
and then flat (reverse hinge) (M4).

**Gain.** What Maxent maximises: how much better the presences score than the background, minus a penalty for
complexity. e raised to the gain is how many times more likely an average presence is than an average background cell
(M5).

**Jackknife.** Extra models with each variable alone and without each variable, to show what each variable knows on
its own and what only it knows (M7).

**MESS (multivariate environmental similarity surface).** How far each cell of a projection area lies outside the
training conditions; negative values mean at least one variable is outside the training range (M10).

**Omission rate.** The share of presences predicted below a threshold. On test records it shows whether the model
transfers to new places (M6, M8).

**Permutation importance.** How much training AUC drops when one variable's values are shuffled; a property of the
final model (M7).

**Percent contribution.** How much each variable raised the gain while the model was being fitted; it depends on the
order in which features were picked (M7).

**Presence-only data.** Records of where a species was seen, without records of where it was looked for and not
found (M1, M2).

**Prior.** What the model expects before it sees the records: by default every cell of the background equally likely;
with a bias file, cells in proportion to sampling effort (M1, M8).

**Pseudo-absence.** An ambiguous term for background points; this course avoids it.

**Regularisation.** A penalty on complexity that keeps only features that really improve the model. The
**regularisation multiplier** (1 by default) scales it: higher values give simpler models (M4, M8).

**Relative occurrence rate (ROR).** Maxent's raw output: values that sum to one over the background (M4).

**Response curve.** How the prediction changes along one variable, with the others at their average (marginal) or in
a model with that variable alone (M7).

**Sampling bias.** Records come more from places that were searched more — near roads, towns and well-known parks —
so a model can learn where people looked instead of where the species lives (M2, M8).

**Spatial thinning.** Keeping one record per cell (here 1 km) to reduce the weight of heavily surveyed sites (M2).

**Target-group sampling.** Using records of related species collected the same way (here GBIF mammal records) to
estimate sampling effort, assuming those observers would have reported the focal species too (M8).

**Threshold.** A cut-off that turns the continuous output into suitable / not suitable. The result depends strongly
on the threshold, so report several (M9).
