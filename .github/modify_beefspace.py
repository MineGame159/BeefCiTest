import toml

space = toml.load("BeefSpace.toml")

for project_name in space["Projects"]:
    project = space["Projects"][project_name]

    if type(project) is str:
        space["Projects"][project_name] = {
            "Path": "Beef/BeefLibs/" + project_name,
        }

with open("BeefSpace.toml", "w") as f:
    f.write(toml.dumps(space))