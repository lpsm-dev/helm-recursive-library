<div align="center">

<p>
  <img alt="gif-header" src="https://cdn.hackernoon.com/hn-images/0*KyeIBTwEiX6_sE06" width="350px" float="center"/>
</p>

<h2 align="center">✨ Helm Chart Library ✨</h2>

<div align="center">

[![Semantic Release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/lpmatos/helm-library)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://github.com/lpmatos/helm-library)
[![GitHub repo size](https://img.shields.io/github/repo-size/lpmatos/helm-library)](https://github.com/lpmatos/helm-library)

</div>

---

<p align="center">
  <img alt="gif-about" src="https://i.stack.imgur.com/niIU6.gif" width="450px" float="center"/>
</p>

<p align="center">
  ✨ This is a simple helm library that i use in GitLab to create recursive resources in Kubernetes ✨
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contributing">Contributing</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#versioning">Versioning</a>
</p>

</div>

---

## ➤ Getting Started <a name = "getting-started"></a>

If you want contribute on this project, first you need to make a **git clone**:

>
> 1. git clone --depth 1 <https://github.com/lpmatos/helm-library.git> -b main
>

This will give you access to the code on your **local machine**.

## ➤ Tools <a name = "tools"></a>

Tools used in this setup:

- kubectl
- helm
- krew
- kubeval
- kube-linter
- kube-score
- checkov
- datree
- kubeaudit

## ➤ Testing <a name = "testing"></a>

Run these commands in the context of `test/chart` folder:

```bash
helm dependency update --debug
helm template . -n valida -f values.yaml > manifest.yml
kubeval manifest.yml --strict --force-color --exit-on-error
kube-linter lint manifest.yml --config .kube-linter.yml
kubectl score manifest.yml
checkov -f manifest.yml --framework kubernetes
datree test manifest.yml
kubeaudit all -f manifest.yml
```

## ➤ Author <a name = "author"></a>

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

>
> * Email: lpsm-dev@protonmail.com
> * Website: <https://github.com/lpmatos>
> * GitHub: [@lpmatos](https://github.com/lpmatos)
> * GitLab: [@lpmatos](https://gitlab.com/lpmatos)
>

## ➤ Versioning <a name = "versioning"></a>

To check the change history, please access the [**CHANGELOG.md**](CHANGELOG.md) file.

## ➤ Troubleshooting <a name = "troubleshooting"></a>

If you have any problems, please contact [me](https://github.com/lpmatos).

## ➤ Project status <a name = "project-status"></a>

Currently the project is constantly being updated 👾.

## ➤ Show your support <a name = "show-your-support"></a>

<div align="center">

Give me a ⭐️ if this project helped you!

<p>
  <img alt="gif-header" src="https://www.icegif.com/wp-content/uploads/baby-yoda-bye-bye-icegif.gif" width="350px" float="center"/>
</p>

Made with 💜 by [me](https://github.com/lpmatos) :wave: inspired on [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

</div>
