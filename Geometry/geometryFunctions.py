






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

def calcSphereBluntedOgiveNose(rho,R,r_n):
  """
  Calculates the 3 points defining the arc for the spherically blunted ogive nose.
  Reference: https://en.wikipedia.org/wiki/Nose_cone_design
  input:

  returns:
    1st point: center point of the circle defining the arc (x_0,y_0)
    2nd point: the front point of the nose (x_a,y_a)
    3rd point: the tangency point of the sphere with the ogive curve of the nose (x_t,y_t)
  """
  L = calcTangentOgiveLength(rho,R)
  y_0 = 0.0
  x_0 = L - ((rho-r_n)**2-(rho-R)**2)**(1/2)
  y_t = r_n*(rho-R)/(rho-r_n)
  x_t = x_0 - (r_n**2-y_t**2)**(1/2)
  y_a = 0.0
  x_a = x_0 - r_n
  return (x_0,y_0), (x_t,y_t), (x_a,y_a)