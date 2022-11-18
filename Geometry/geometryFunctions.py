






def calcTangentOgiveRadius(L,R):
  """
  Calculates the tangent ogive radius length based on R and rho.
  Reference: https://en.wikipedia.org/wiki/Nose_cone_design
  """

  return (R**2+L**2)/(2*R)

def calcTangentOgiveLength(rho,R):
  """
  Calculates the tangent ogive base length based on R and rho.
  Reference: https://en.wikipedia.org/wiki/Nose_cone_design
  """
  
  return (2*R*rho-R**2)**(1/2)
  
def calcTangentOgiveY(rho,R,x):
  """
  Calculates the radius y along the tangent ogive based on the axial length x.
  Reference: https://en.wikipedia.org/wiki/Nose_cone_design
  """
  L = calcTangentOgiveLength(rho,R)
  
  return (rho**2-(L-x)**2)**(1/2)+R-rho

def calcTangentOgiveX(rho,R,y):
  """
  Calculates the axial length x based on the radiual value y along the tangent ogive.
  Reference: https://en.wikipedia.org/wiki/Nose_cone_design
  """
  L = calcTangentOgiveLength(rho,R)
  return L - (rho**2-(rho+y-R)**2)**(1/2)
