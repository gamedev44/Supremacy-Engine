# 🎮 Supremacy Engine 🛠️

Supremacy Engine is a (Semi) Open-Source **Python 3D engine** built on **PyOpenGL**, with **Pygame** and **Pyglet** backends. It’s designed for real-time rendering, physics, and advanced graphics experimentation.

---

## 📖 Table of Contents

* [System Requirements](#💻-system-requirements)
* [Troubleshooting Anaconda Crash](#🛠️-troubleshooting-anaconda-crash)
* [Features](#🚀-features)

  * [Importers](#importers)
  * [Lighting](#lighting)
  * [Particle System](#particle-system)
  * [Objects](#objects)
  * [Rendering](#rendering)
  * [Resource Management](#resource-management)
  * [GUI](#gui)
  * [Optimizations](#optimizations)
* [Coming Soon / Planned](#🔮-coming-soon--planned)

---

## 💻 System Requirements

Ensure the following are installed before running the engine:

* **OpenGL 4.3** (Shading language 430)
* `numpy`
* `pillow`
* `pyglet` or `pygame`
* `PyOpenGL`
* `PyOpenGL-accelerate` (optional)

**Supported Platforms**: Windows and Linux (Mac untested)

---

## 🛠️ Troubleshooting Anaconda Crash

If you encounter:

```
ImportError: DLL load failed
```

It is often caused by a conflict with the `Pillow` library.

### Solutions:

**1️⃣ Install from Anaconda channel**

```bash
conda install -c anaconda pillow
```

**2️⃣ Install a specific version via conda-forge**

```bash
conda install -c conda-forge pillow=5
```

**3️⃣ Reinstall using pip**

```bash
conda remove pillow
pip install pillow
```

---

## 🚀 Features

### Importers

* **Mesh**: `.obj`, `.dae` (Collada). Planned: `.fbx`, `.gltf`, `.blend`
* **Texture**: `.png`, `.tga`, `.bmp`, `.jpeg`. Compressed formats ETC & DDS planned

### Lighting

* ✅ **Directional Light** & Shadow Mapping
* ❌ Spot Light
* ❌ Area Light
* ✅ **Point Light**

### Particle System

* ✅ **CPU-Based Particle**
* ✅ **GPU-Based Particle**
  ![GPU Particles](https://github.com/user-attachments/assets/7740af2a-e6cf-48cc-8558-2686519597a1)
* ✅ **Vector Field**
* ❌ Particle spawn on polygon surface
* ❌ Bitonic Sorting
* ❌ Memory Pool
* ❌ Attractor
* ❌ Noise
* ❌ Curl Noise

### Objects

* ❌ Select, Move, Modify
* ❌ Gizmo
* ✅ **Skeleton Mesh**
* ✅ **Static Mesh**
* ❌ Tree, Foliage, Grass
* ✅ **Terrain**
  ![Terrain](https://github.com/user-attachments/assets/c009ec2e-e137-4c70-8b14-87269452eb27)
* ✅ **Atmosphere & Sky**
  ![Sky](https://github.com/user-attachments/assets/129a1715-3cee-4182-986e-9cea3f77834b)
* ❌ Road
* ❌ Wind
* ✅ **FFT Ocean**
  ![Ocean](https://github.com/user-attachments/assets/6d75d5e6-e03e-477e-b033-fe233beff669)
* ❌ River

### Rendering

* **Culling**

  * ❌ Occlusion Culling
  * ❌ Distance Culling
  * ✅ **View Frustum Culling**
* ❌ VTF Skinning
* ❌ GPU Animation
* ❌ Distance Field Font
* ✅ **Real-time Light Probe**
* ✅ **PBR** (Physically Based Rendering)
  ![PBR](https://github.com/user-attachments/assets/07f343ec-4d4d-48a0-81d9-9aa5919568ae)
* ✅ **Temporal AA**
* ✅ **SSAA**
* ✅ **MSAA**
* ❌ Temporal Upscale
* ✅ **Screen Space Reflection**
* ✅ **Screen Space Ambient Occlusion**
* ❌ Screen Space Bevel
* ❌ Screen Space SSS
* ✅ **Depth Of Field**

  * ❌ Bokeh
* ✅ **Bloom**
* ✅ **Tone Mapping**
* ❌ Glare
* ❌ Film Grain
* ❌ Color Correction
* ❌ Color Grading
* ✅ **Light Shaft**
  ![Light Shafts](https://github.com/user-attachments/assets/2bc3935d-ee7d-492e-81f8-7a26b175e4dc)
* ✅ **Motion Blur**

  * ❌ Recursive Velocity
* ❌ Parallax Occlusion Rendering
* ❌ Paraboloid environment map
* ❌ Voxel Based GI
* ❌ Volumetric Scattering
* ❌ Fur Rendering

### Resource Management

* ✅ Load / Save / Import / Export
* ❌ Unload / Reload system
* ❌ Duplicate resource
* ❌ Sound Manager
* ✅ Script Manager

### GUI

![GUI](https://github.com/user-attachments/assets/a44ba44b-c801-4b93-8cf0-2fc8c1dc4cc5)

* ❌ Input / Output
* ❌ Progress Bars
* ❌ Buttons

### Optimizations

* ❌ Only dynamic shadows updated every frame
* ❌ SSR ray reuse in compute shader
* ❌ Post-processing in compute shader
* ❌ FFT in compute shader
* ❌ Precomputed atmosphere in compute shader

---

## 🔮 Coming Soon / Planned

* **Blender3D Plugin** – Transfer geometry, animation, and scene data
* **Bullet Physics** – Realistic physics integration
