import gc
print("enabled:", gc.isenabled())
print("thresholds:", gc.get_threshold())
print("counts:", gc.get_count())
