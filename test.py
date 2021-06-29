# %%
with open("/data/fer2013.csv") as f:
    content = f.readlines()
 
lines = np.array(content)
 
num_of_instances = lines.size
print("number of instances: ",num_of_instances)

# %%
