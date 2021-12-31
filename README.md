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
  <a href="#motivation">Motivation</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
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

List of tools thar i used in this project:

- kubectl
- helm
- krew
- kubeval
- kube-linter
- kube-score
- checkov
- datree
- kubeaudit

## ➤ Motivation <a name = "motivation"></a>

Hi stranger! Today I want to share with you my experience using Helm library chart daily on my work, but let's go back to the concepts. Helm is a package maneger that you can use to organize all kubernetes objects created in a cluster, all versioned and based on a standard structure.

Over the time you realize that once you create the helm chart it will hardly have to change its structure. However, depending on your project and the amount of services that you have, this can become a challenge for you.

With that in mind we have the helm libraries, which help you share default settings for your catalogs. And that's what this project proposes: make a helm library for creating objects using recursion, speeding up the setup of your services in Kubernetes.

## ➤ Usage <a name = "usage"></a>

Reference in `Chart.yaml`:

```yaml
dependencies:
- name: common
  version: 0.0.1
  repository: file://../../chart
```

Update local chart:

```bash
helm dependency update
```

## ➤ Audit <a name = "audit"></a>

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

## ➤ Concepts <a name = "concepts"></a>

This section aims to describe at a high level what the tools we use are and how we use them, without reproducing documentation that is better written (and more up to date) in the repositories and websites of these tools themselves. It's recommended to familiarize yourself with these tools as early as possible.

### Helm

Helm is a templating system for Kubernetes resource manifests. A Helm chart is a bundle of resource templates that can take parameters ("values"). A Helm chart therefore describes a paramaterized deployment configuration that is environment-agnostic. Helm charts are distributed from Helm repositories, and Helm can act as a package manager to manage repositories and charts.

An instantiated deployment of a Helm chart is called a Helm release. We'll refer to these as "releases" for short. We can say that a release is a deployment of a Helm chart in an environment, where an environment is the combination of a set of parameters ("values") and a Kubernetes target.

## ➤ Inspirations <a name = "inspirations"></a>

- https://github.com/InsomniaCoder/helm-library
- https://github.com/k8s-at-home/library-charts
- https://github.com/prefapp/prefapp-helm
- https://github.com/wuguteng/propeller

## ➤ Author <a name = "author"></a>

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

>
> * Email: lpsm-dev@protonmail.com
> * Website: https://linktr.ee/lpmatos
>

## ➤ Versioning <a name = "versioning"></a>

To check the change history, please access the [**CHANGELOG.md**](CHANGELOG.md) file.

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
