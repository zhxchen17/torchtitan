# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from dataclasses import dataclass, field


@dataclass
class Compile:
    model_backend_override: str | None = None
    """Override backend to compile in simplefsdp. Additional backend includes aot_eager_autobucketing """

    manual_bucketed_modules: list[str] = field(default_factory=list)
    """
    Manual bucket modules based on user specified FQNs
    Abbreviations are supported to make specifying modules easier.
    Currently, the following abbreviations are available:
    (1) layers.[0-2] -> [layers.0], [layers.1], [layers.2]
        (layers are split three separate buckets)
    (2) norm+output -> [norm, output]
        (norm and output are in one bucket)
    """


@dataclass
class JobConfig:
    compile: Compile = field(default_factory=Compile)
