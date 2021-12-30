import os

import fire
import yaml


def change_chart(path, version):
    for root, _, files in os.walk(path, topdown=False):
        for file in files:
            if file == "Chart.yaml":
                with open(os.path.join(root, file), "rt") as helm:
                    try:
                        lyaml = yaml.safe_load(helm)
                        current_version = lyaml["version"]
                        print(f"==> ✨ Current version: {current_version}")
                    except Exception as err:
                        print(err)
                print(f"==> ✨ New version: {version}\n")
                lyaml["version"] = version
                if version == current_version:
                    print("==> 🚧 No changes in version\n")
                    break
                with open(os.path.join(root, file), "w") as helm:
                    yaml.dump(lyaml, helm)


if __name__ == "__main__":
    fire.Fire(change_chart)
