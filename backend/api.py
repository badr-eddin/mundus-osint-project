from core.composer import mundus
from core.io.domains import categories


mnd = mundus()

# finding names
params = {
    "max": 1,
    "exact": False
}

results = mnd.track_person_by_name(name="ksi", **{"google": params})