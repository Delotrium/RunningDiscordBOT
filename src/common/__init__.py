from pint import UnitRegistry


Units = UnitRegistry()

Units.define('@alias degC = celcius')
Units.define('@alias degC = cel')
Units.define('@alias degC = c')
Units.define('@alias degC = C')
Units.define('@alias degF = fahrenheit')
Units.define('@alias degF = f')
Units.define('@alias degF = F')

Q_ = Units.Quantity
U_ = Units.Unit