# AI Rider Roadmap

## Project Vision

AI Rider is a hybrid Digital Signal Processing (DSP) and Artificial Intelligence (AI) vocal enhancement system designed to automatically improve speech recordings while preserving the speaker's natural performance.

The long-term goal is to create an intelligent audio engineer capable of:

* Removing unwanted recording artifacts
* Preserving natural dynamics
* Automatically balancing loudness
* Using AI to make engineering decisions
* Producing professional-quality spoken audio

---

# Version 2 – DSP Foundation (Current)

## Analysis

* [x] Voice Detection
* [x] Loudness Measurement
* [x] Wind Detection
* [x] Plosive Detection
* [x] Airflow Ratio Detection
* [x] Gain Analysis

---

## Processing

* [x] Automatic Vocal Rider
* [x] Gain Smoothing
* [x] Wind Reduction
* [x] Plosive Reduction

---

## Current Milestones

### 2.24 – Frequency Processing Framework

* [ ] Low-pass filter
* [ ] High-pass filter
* [ ] Band-pass filter
* [ ] Filter testing utilities

---

### 2.25 – Frequency-Based Wind Reduction

* [ ] Replace full-band attenuation
* [ ] Reduce only low-frequency wind energy
* [ ] Preserve vocal body

---

### 2.26 – Frequency-Based Plosive Reduction

* [ ] Apply frequency-selective reduction
* [ ] Preserve consonant clarity
* [ ] Reduce popping artifacts

---

### 2.27 – Dynamic De-Esser

* [ ] Use airflow ratio detection
* [ ] Detect excessive sibilance
* [ ] Reduce only high-frequency sibilance

---

### 2.28 – Breath Reduction

* [ ] Detect breaths
* [ ] Reduce breath intensity
* [ ] Preserve natural speech pacing

---

### 2.29 – Limiter

* [ ] Peak limiting
* [ ] Clip protection
* [ ] Final output safety

---

### 2.30 – Loudness Normalization

* [ ] Consistent export loudness
* [ ] Configurable loudness targets

---

### 2.31 – Pipeline Optimization

* [ ] Optimize processing order
* [ ] Reduce redundant processing
* [ ] Improve efficiency

---

### 2.32 – Configuration System

* [ ] Central settings file
* [ ] Adjustable processing strengths
* [ ] Enable/disable individual modules

---

### 2.33 – Automation Slider

User-controlled processing amount.

Range:

0%

* Preserve natural dynamics
* Minimal processing

100%

* Maximum consistency
* Broadcast-style sound

---

### 2.34 – Performance Optimization

* [ ] Faster processing
* [ ] Lower memory usage
* [ ] Cleaner module architecture

---

# Version 3 – AI Integration

## 3.0 AI Noise Cleanup

* Integrate pretrained AI noise reduction
* Remove room noise
* Remove background distractions

Potential models:

* DeepFilterNet
* Demucs
* RNNoise

---

## 3.1 AI Parameter Selection

Use AI to analyze recording characteristics and recommend:

* Wind reduction strength
* Plosive reduction strength
* Vocal riding amount
* De-esser strength
* Loudness targets

DSP remains responsible for applying the processing.

---

## 3.2 Intelligent Automation

The Automation Slider becomes AI-driven.

AI determines how much natural dynamics should be preserved based on:

* Speech style
* Recording quality
* Vocal consistency
* Intended output

---

## 3.3 Context-Aware Audio Processing

Future research:

* Detect emphasis
* Preserve intentional pauses
* Preserve emotional dynamics
* Adapt processing to speaking style

---

# Long-Term Vision

Create an intelligent virtual audio engineer capable of producing studio-quality spoken audio with minimal user input while remaining fully modular, allowing both traditional DSP algorithms and AI models to evolve independently.
