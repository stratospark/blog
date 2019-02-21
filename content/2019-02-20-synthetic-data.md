Title: Generating Synthetic Data for Image Segmentation with Unity and PyTorch/fastai
Date: 2019-02-20 15:30
Category: programming
Tags: unity, deep learning, fastai, pytorch
Slug: generating-synthetic-data-image-segmentation-unity-pytorch-fastai
Authors: Patrick Rodriguez
Summary: ![Image Synthesis Intro]({attach}/images/synthetic-data/image-synthesis-intro.jpg) This article and video tutorial will help you get up to speed with generating synthetic training images in Unity. You don't need any experience with Unity, but experience with Python and the fastai library/course is recommended. By the end of the tutorial, you will have trained an image segmentation network that can recognize different 3d solids. 

![Image Synthesis Intro]({attach}/images/synthetic-data/image-synthesis-intro.jpg)

This article will help you get up to speed with generating synthetic training images in Unity. You don't need any experience with Unity, but experience with Python and the fastai library/course is recommended. By the end of the tutorial, you will have trained an image segmentation network that can recognize different 3d solids. Read on for more background, or jump straight to the [video tutorial](https://www.youtube.com/watch?v=P4CCMvtUohA&feature=youtu.be) and [GitHub repo](https://github.com/stratospark/UnityImageSynthesisTutorial1).

* [Background](#background)
* [Tutorial](#tutorial)
* [Next Steps](#next-steps)

### <a name="background"></a> Background 

When training neural networks for computer vision tasks, you can’t get away from the need for high-quality labeled data… and _lots_ of it. Sometimes, there is a freely available dataset that is up for the task. Other times, we are lucky enough to have other parts of an organization managing the data collection and labeling infrastructure. For those cases where you just can’t get enough labeled data, don’t despair! Research shows that we can obtain state of the art results with synthetic data (reducing or eliminating the need for actual training data).

In this overview of Deep Learning advances of the past 2 years, Lex Fridman reserves a section for the topic of training with Synthetic Data, particularly domain randomization techniques: 

[![Lex Fridman - Synthetic Data Slide]({attach}/images/synthetic-data/fridman-synthetic.jpg )](https://www.youtube.com/watch?v=53YvP6gdD7U&feature=youtu.be&t=1371)


**Domain Randomization** is like image augmentation on steroids, and then some. Given some base images or 3D models, we use a 3D graphics engine to generate many different versions of a scene: randomized colors, textures, positions, scales, rotations, morphs, lighting conditions, camera angles, etc. Since the engine is generating these scenes, it can simultaneously generate the appropriate labels, such as bounding boxes or segmentation masks.

Possible 3D engine choices include [Unity](https://unity3d.com/), [Unreal Engine](https://www.unrealengine.com), and [Blender](https://www.blender.org/). Unity and Unreal are game engines, which power some of the most popular games out there. Games need to run in real-time (> 30FPS) and many strive for more and more realistic graphics each year. In other words, perfect for quickly generating many synthetic images for training purposes. It’s awesome that indie developers, researchers, and programmers of all stripes are able use the same tools as pro game developers, at no to low-cost. Blender is different in that it is an open-source 3D modeling and animation tool. Though it has some capabilities for real-time rendering, the main use case is for offline rendering, where a frame can take seconds, minutes, or even hours to render depending on scene complexity. What it lacks in speed, it makes up for in more realistic renderings and the ability to use Python as a scripting language.

I’m going to focus on Unity, only because I am most familiar with it. Coming from an applications and data engineering background, it can be daunting to dive into using a game engine. There are so many features and APIs in Unity, it’s easy to get overwhelmed. Remember that building modern games are a complex endeavor, encompassing many specialized fields such as 3D graphics, animations, physics, sound, networking, real-time performance optimizations, UI/UX design, level design, etc. Luckily, there is just a subset of functionality that we need to start generating synthetic data.

Unity provides an open-source package: [Image Synthesis for Machine Learning](https://bitbucket.org/Unity-Technologies/ml-imagesynthesis). It’s the perfect base to start building synthetic image generators. Take a look at their sample screenshot of a simulated driving environment, and the different annotations that are automatically extracted. The included scripts can save each frame to disk, along with the multiple annotations per frame.

![Example driving scene segmentation]({attach}/images/synthetic-data/unity-image-synth-car.jpg)

The project does not actually include the car simulator, and the actual example it does come with is not suitable for generating training data. I would like to provide a short tutorial showing how to both generate data for a toy problem *and* use that data to train an image segmentation neural network. In future posts, I hope to enhance our example with more domain randomization techniques and move from toy problems to more sophisticated ones.

### <a name="tutorial"></a> Tutorial

A source of inspiration has been the course ["Practical Deep Learning for Coders, v3” from fast.ai](https://course.fast.ai/). For those who haven’t taken any of their courses, I highly recommend them for their hands-on, top-down approach to learning. You’ll learn how to use their incredible [fastai library](https://docs.fast.ai/) for PyTorch, allowing you to tackle a diverse set of complex tasks with the same well-designed API: image classification, object detection, image segmentation, regression, text classification, just to name a few. 

In [lesson 3](https://docs.fast.ai/) of their latest course, you learn how to train U-Net based segmentation network on the CamVid street scene dataset. The network will learn how to identify which pixels belong to which classes, including Road, Car, Pedestrian, Tree, etc.

The toy problem that I came up involves being able to segment an image to find geometric solids such as Cubes, Spheres, and Cylinders. These are simple 3D models that are actually built into Unity.

**Requirements:**

* Unity installed, preferrably version 2018.3.2
* Python environment with fastai and dependencies installed

_The tutorial is mainly in video form due to the GUI driven editor of Unity. Also, many readers are coming from the machine learning world, so I'm assuming they have little to no experience using Unity and would appreciate a bit of hand-holding. Don't worry though, we quickly get into the actual task at hand after some preliminaries._

You can [clone the repo](https://github.com/stratospark/UnityImageSynthesisTutorial1) and run the final project, or follow along with the video to recreate the project from scratch.

<iframe width="560" height="315" src="https://www.youtube.com/embed/P4CCMvtUohA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For convenience, the following is a list of some of the topics we'll cover in the video:

1. Downloading the ML-ImageSynthesis code and exploring its functionality
1. Basic components of the Unity Editor GUI and how to customize it
1. Organizing a Unity project with appropriate folders
1. Creating new Scenes
1. Creating new GameObjects, specifically 3d solids like Cubes, Spheres, and Cylinders
1. Manipulating objects in the Scene view, including positioning, rotating, and scaling with mouse and keyboard
1. Using the Inspector pane to modify public properties of GameObject components
1. The difference between Scene and Game views and how to adjust the Camera
1. Creating user-defined Layers to act as object categories
1. Creating and modifying Prefabs
1. Creating a custom C# component script
1. Exposing script variables to the Editor GUI
1. Visually linking components to each other in the GUI
1. Adding custom camera display resolutions
1. Modifying object appearance with custom Materials
1. Enabling the Physics Engine and how RigidBodies work
1. The Start/Update methods of MonoBehavior subclasses
1. Randomizing the position/rotation/scale/color of a GameObject through code
1. Inspecting memory usage with the Profiler
1. Creating an Object Pooling system to reuse objects and cap memory usage
1. Modifying ImageSynthesis code to output only a specific annotation image
1. Creating fields to specify # of training and validation images in the Editor
1. Modifying the layer colors to conform to the grayscale RGB values the image segmentation network requires
1. Using the fastai Datablock API to load data produced by our Unity simulation


### <a name="next-steps"></a> Next Steps

There are a lot of ways we can go from here. For example, randomizing:

* Textures, instead of flat colors
* Lighting conditions, including multiple light sources, varying intensities, and colors
* HDR imagery to provide realistic backgrounds and lighting
* Camera angles and properties such as FOV

I'd like to extend our simulator to handle some of these properties in future posts. Not to mention, seeing how well a network trained on simulated images does on real world data!

**Do you know of any datasets where you'd like try creating simulated images and apply domain randomizaiton?**

In the mean time, here is an early paper on the topic to help you dive deeper. Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World:

[![Domain Randomization Paper]({attach}/images/synthetic-data/domain-randomization-paper.jpg)](https://arxiv.org/abs/1703.06907)

