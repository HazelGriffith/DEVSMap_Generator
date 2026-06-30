# DEVSMap_Generator

## Introduction
DEVSMap Generator accepts DEVS model information and generates files in the DEVSMap format that match the DEVS model provided. We provide an abstract DEVSMap Generator class  following the Template design pattern for users to define their own DEVSMap Generator given the DEVS model information they are starting with.

## Short-term Goals
The end goal of this project is to generate axioms that correctly and completely describe DEVS models of any type and complexity

- [&check;] Create abstract DEVSMap generator class for DEVS atomic models
    - [&check;] Create abstract methods for generating each section of DEVSMap atomic model
    - [&check;] Create concrete method for saving atomic model object map as JSON file
    - [&check;] Create concrete method that enforces order of generation algorithm in accordance with the Template design pattern
- [ ] Create abstract class(es) for Sets and Parameters file generation
- [ ] Complete unit testing

## Long-term Goals

- [ ] Create example derived DEVSMap generator from open source model data
