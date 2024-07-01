from OMPython import OMCSessionZMQ, ModelicaSystem
import pandas as pd
import numpy as np


omc = OMCSessionZMQ()
print("Initializing OMCSessionZMQ")
mod = ModelicaSystem(
    fileName="C:\\Users\\Rocco\\AppData\\Roaming\\.openmodelica\\libraries\\Archetype\\package.mo",
    modelName="Archetype.Examples.RadiatorSetpoint",
    lmodel=["Modelica", "Buildings"],
    verbose=True)

print("Uploaded model")

mod.setSimulationOptions([f"stopTime={86400*2}", "stepSize=300"])
mod.setParameters(["envelopeModel.gWin=0.1"])
mod.simulate()

sol = mod.getSolutions(["time", "envelopeModel.TAir"])
df = pd.DataFrame(sol.T, columns=["time", "envelopeModel.TAir"])
df["time"] = df["time"].round(1)
df = df.drop_duplicates(subset=["time"])
array_time = np.arange(0, 86400*2, 300.0)
df_sub = df[df["time"].isin(array_time)]
