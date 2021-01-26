using Plots
using DataFrames
using StatsPlots

df = DataFrame(
    fruit   = ["orange", "orange", "orange", "orange", "apple", "apple", "apple", "apple"],
    year    = [2010, 2011, 2012, 2013, 2010, 20,11, 2012, 2013]
)

pyplot()



#=
using DataFrames, Plots, StatsPlots
df = DataFrame(
  fruit       = ["orange","orange","orange","orange","apple","apple","apple","apple"],
  year        = [2010,2011,2012,2013,2010,2011,2012,2013],
  production  = [120,150,170,160,100,130,165,158],
  consumption = [70,90,100,95,   80,95,110,120]
)
pyplot()
mycolours = [:green :orange] # note that the serie is piled up alphabetically
@df df plot(:year, :production, group=:fruit, linestyle = :solid, linewidth=3, label = reshape(("Production of " .* sort(unique(:fruit))),(1,:)), color=mycolours)
@df df plot!(:year, :consumption, group=:fruit, linestyle = :dot, linewidth=3, label = reshape(("Consumption of " .* sort(unique(:fruit))),(1,:)), color=mycolours)
=#