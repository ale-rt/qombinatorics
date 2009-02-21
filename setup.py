#!/usr/bin/env python
from distutils.core import setup

setup(name = "qombinatorics",
      version = "0.2",
      description = "qombinatorics - a combination and permutation calculator",
      author = "Alessandro Pisa",
      author_email = "alessandro...pisa@@@gmail...com",
      url = "http://darkmoon.altervista.org",
      packages = ["qombinatorics", ""],
      scripts = ['scripts/qombinatorics'],
      long_description = """
qombinatorics aims to be a complete resource for combinatorics calulations.

Combinatorics, in mathematic, is the study of the many possible way to arrange a given set of objects. (http://en.wikipedia.org/wiki/Combinatorics)

Many probability calculation are possible through the knowledge of this branch of mathematics and can be easily applied to a great number of common situation, e.g. card games.
"""
)
