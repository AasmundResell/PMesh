from math import *

def Re(U,L,rho,mu):
    return (U*L*rho)/mu

def IdealGasLawAir(P,T):
    R = 0.286 #kJ/kg/K, constant for air
    return P/(R*T)

def SkinFrictionCoeff(Re, method="schlichting"):
    """
    https://www.cfd-online.com/Wiki/Skin_friction_coefficient
    """
    print("Reynolds number determining the skin friction coefficient is: ",Re)
    if method.lower() == "schlichting":
        if Re < 10**9:
            return (2*log10(Re)-0.65)**(-2.3)
        else:
            ValueError("Schlichting skin friction coefficient invalid for Re above 10⁹")
    elif method.lower() == "power_law":
        if Re < 10**9 and Re > 5*10**5:
            return 0.0576*Re**(-1/5)
        else:
            ValueError("Power law skin friction coefficient invalid for Re below 5*10⁵ and above 10⁷")
    elif method.lower() == "power_law_calibrated":
        if Re < 10**9 and Re > 5*10**5:
            return 0.0592*Re**(-1/5)
        else:
            ValueError("Power law skin friction coefficient invalid for Re below 5*10⁵ and above 10⁷")


def YPlus(y_plus,U,L,rho,mu,skinFrictionMethod = "power_law_calibrated"):
    """
    https://www.cfd-online.com/Wiki/Y_plus_wall_distance_estimation
    """
    Cf = SkinFrictionCoeff(Re(U,L,rho,mu),skinFrictionMethod)
    tau_w = Cf*1/2*rho*U**2 #Wall shear stress
    u_star = (tau_w/rho) #Friction velocity
    return (y_plus*mu)/(rho*u_star)

def BLThicknessFromCellHeight(y_initial,num_cells,growth_rate):
    """
    https://www.youtube.com/watch?v=1gSHN99I7L4&ab_channel=FluidMechanics101
    """
    y_h = y_initial*2 #Total heigh of first boundary layer cell
    return y_h*(1-growth_rate**(num_cells))/(1-growth_rate)

def BLThicknessFromTheory(Re,L,method = "cengel_cimbala"):
    """
    https://www.youtube.com/watch?v=1gSHN99I7L4&ab_channel=FluidMechanics101
    """
    if method.lower() == "cengel_cimbala":
        if Re < 5*10**5:
            return 4.91*L*Re**(-1/2)
        elif Re > 5*10**5:
            return 0.38*L*Re**(-1/5)
    else:
        RuntimeError("Invalid method specified for calculating boundary layer thickness")
  

if __name__ == "__main__":
    #Testing the mesh tools

    U = 343
    rho = 1.225
    mu = 18.5*10**(-6)
    L = 75.9/1000 
    print("L: ",L)
    yplus_target = 30.0
    G = 1.2 #Growth rate
    n = 20 #number of bl cells
    y_init = YPlus(yplus_target, U, L, rho, mu, skinFrictionMethod="Schlichting")

    totalHeightCalculated = BLThicknessFromCellHeight(y_init,n,G)

    totalHeightTheory = BLThicknessFromTheory(Re(U,L,rho,mu),L)

    print(y_init*1000)
    print(totalHeightCalculated*1000)
    print(totalHeightTheory*1000)