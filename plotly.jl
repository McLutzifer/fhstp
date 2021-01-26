using Plotly



trace1 = [
  "x" => [0, 4, 8, 10, 12, 14],
  "y" => [0, 83.3, 167, 208, 250, 292],
  "name" => "Verhältnis U zu I",
  "type" => "scatter"
]
trace2 = [
  "x" => [0, 1, 2, 3, 4, 5, 6, 7, 8],
  "y" => [1, 0, 3, 2, 5, 4, 7, 6, 8],
  "name" => "Name of Trace 2",
  "type" => "scatter"
]
data = [trace1, trace2]
layout = [
  "title" => "Verhältnis Spannung zu Stromstärke in der Glühbirne",
  "xaxis" => [
    "title" => "x Axis",
    "titlefont" => [
      "family" => "Courier New, monospace",
      "size" => 18,
      "color" => "#7f7f7f"
    ]
  ],
  "yaxis" => [
    "title" => "y Axis",
    "titlefont" => [
      "family" => "Courier New, monospace",
      "size" => 18,
      "color" => "#7f7f7f"
    ]
  ]
]
response = Plotly.plot(data, ["layout" => layout, "filename" => "styling-names", "fileopt" => "overwrite"])
plot_url = response["url"]
