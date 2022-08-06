# AUTOGENERATED! DO NOT EDIT! File to edit: ../ttbarzp.ipynb.

# %% auto 0
__all__ = ['get_elijah_ttbarzp_cs', 'get_manuel_ttbarzp_cs', 'import47Ddata', 'get47Dfeatures']

# %% ../ttbarzp.ipynb 3
import numpy as np
import tensorflow as tf

# %% ../ttbarzp.ipynb 5
def get_elijah_ttbarzp_cs():
    r"""
    Contains cross section information produced by Elijah for $pp \to t\overline{t} \; Z'$ collider phenomenology.
    
    Returns list containing signal masses, signal cross sections (for those masses, in pb), and background cross sections 
    (also in pb)
    """
    # Z' masses (GeV) for which Elijah created signal samples
    elijah_masses = [10, 50, 100, 200, 350, 500, 1000, 2000, 5000]
    # signal cross sections (pb)  
    elijah_sig_css = [9.801, 0.5445, 0.1442, 0.03622, 0.009998, 0.003802, 0.0003936, 2.034e-05, 2.748e-08]
    # background cross sections (pb)
    elijah_bg_css = [0.106, 0.0117, 5.58]
    return [elijah_masses, elijah_sig_css, elijah_bg_css]

# %% ../ttbarzp.ipynb 6
def get_manuel_ttbarzp_cs():
    r"""
    Contains cross section information produced through MadGraph by Manuel for collider phenomenology regarding
    the semihadronic, semileptonic $pp \to t\overline{t} \; Z', Z' \to b\overline{b}$ channel
    """
    # Z' masses (GeV) for which I (Elijah) created signal samples
    manuel_masses = [350, 500, 750, 1000, 2000, 3000, 4000]
    # signal cross sections (pb)  
    manuel_sig_css = [0.001395, 0.0007823, 0.0003429, 0.0001692, 1.808e-05, 1.325e-06, 4.456e-07]
    # background cross sections (pb)  
    manuel_bg_css = [0.1339, 0.01187, 5.603]
    return [manuel_masses, manuel_sig_css, manuel_bg_css]

# %% ../ttbarzp.ipynb 7
def import47Ddata(name):
    r"""
    Imports `name.npy` file containing 47-dimensional data for training

    Available files:
     - bgh.npy (Standard Model background 1, $pp \to t\overline{t}h$)
     - bg4t.npy (Standard Model background 2, $pp \to t\overline{t}t\overline{t}$)
     - bgnoh.npy (Standard Model background 3, $pp \to t\overline{t} \; \setminus \; h$)
     - sig350G.npy ($Z'$ signal, $m_{Z'} = 350$ GeV)
     - sig500G.npy ($Z'$ signal, $m_{Z'} = 500$ GeV)
     - sig1T.npy ($Z'$ signal, $m_{Z'} = 1$ TeV)
     - sig2T.npy ($Z'$ signal, $m_{Z'} = 2$ TeV)
     - sig4T.npy ($Z'$ signal, $m_{Z'} = 4$ TeV)
    """

    if name[-4:] == '.npy':
        name = name[:-4]           
    url = 'https://storage.googleapis.com/ttbarzp/47dim/'
    try: 
        path = tf.keras.utils.get_file(f'{name}.npy', url + name + '.npy')
        data = np.load(path)
        return data
    except:
        print(f"{name}.npy doesn't appear to exist")

# %% ../ttbarzp.ipynb 8
def get47Dfeatures():
    """
    Returns list containing the names of the 47 features found in the data accessible through 
    `ttbarzp.import47Ddata()`
    """
    return [
        'pT b1', 'pT b2', 'pT b3', 'pT b4',
        'sdEta b1 b2', 'sdEta b1 b3', 'sdEta b1 b4', 'sdEta b2 b3', 'sdEta b2 b4', 'sdEta b3 b4',
        'sdPhi b1 b2', 'sdPhi b1 b3', 'sdPhi b1 b4', 'sdPhi b2 b3', 'sdPhi b2 b4', 'sdPhi b3 b4',
        'dR b1 b2', 'dR b1 b3', 'dR b1 b4', 'dR b2 b3', 'dR b2 b4', 'dR b3 b4',
        'MET', 'pT l', 'MT l MET', 
        'M b1 b2', 'M b1 b3', 'M b1 b4', 'M b2 b3', 'M b2 b4', 'M b3 b4',
        'MT b1 l MET', 'MT b2 l MET', 'MT b3 l MET', 'MT b4 l MET',
        'M j1 j2', 'pT j1', 'pT j2', 'dR j1 j2', 
        'dR b1 l', 'dR b2 l', 'dR b3 l', 'dR b4 l',
        'sdPhi b1 l', 'sdPhi b2 l', 'sdPhi b3 l', 'sdPhi b4 l']
