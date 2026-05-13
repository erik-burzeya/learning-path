### Plot Styling Cheat-Sheet

*This Cheat-Sheet was created with ChatGPT.*
## 1. Basic Plot Styling
    from matplotlib import pyplot as plt

    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]

    plt.plot(x, y)
    plt.show()

## 2. Change Line Color
    plt.plot(x, y, color='red')
    
    red	    = 'red'
    blue	= 'blue'
    green	= 'green'
    ...

    Hex colors:
    plt.plot(x, y, color='#1f77b4')

## 3. Change Line Style
    plt.plot(x, y, linestyle='solid')
    
    Line styles:
    Solid	    = 'solid'   or '-'
    Dashed	    = 'dashed'  or '--'
    Dotted	    = 'dotted'  or ':'
    Dash-dot    = 'dashdot' or '-.'

## 4. Change Line Width
    plt.plot(x, y, linewidth=3)

## 5. Add Markers
    plt.plot(x, y, marker='o')
   
   Marker styles:
    'o'	= Circle
    's'	= Square
    '^'	= Triangle
    'x'	= X marker
    '*'	= Star
    '.'	= Point

## 6. Marker Size
    plt.plot(x, y, marker='o', markersize=10)

## 7. Marker Colors
    plt.plot(
        x,
        y,
        marker='o',
        markerfacecolor='white',
        markeredgecolor='blue'
    )  

## 8. Add a Title
    plt.title('GDP Growth')

    Font customization: 
    plt.title(
        'GDP Growth',
        fontsize=18,
        fontweight='bold'
    )

## 9. Axis Labels
    plt.xlabel('Year')
    plt.ylabel('GDP')

    Customize labels:
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP', fontsize=12)

## 10. Grid
    plt.grid(True)

    Customize grid:
    plt.grid(
        True,
        linestyle='--',
        alpha=0.5
    )

## 11. Figure Size
    plt.figure(figsize=(10, 5))

    Info:
    (8, 4)	    = Wide
    (6, 6)	    = Square
    (12, 6)	    = Presentation style

## 12. Legends
    plt.plot(x, y, label='GDP')
    plt.legend()

    Legend position:
    plt.legend(loc='upper left')

## 13. Multiple Lines
    x = [1, 2, 3, 4]

    apples = [1, 4, 6, 8]
    oranges = [2, 3, 5, 9]

    plt.plot(x, apples, label='Apples')
    plt.plot(x, oranges, label='Oranges')

    plt.legend()
    plt.show()

## 14. Background Styles
    Built-in styles:
    plt.style.use('ggplot')

    Popular styles:
    'ggplot'
    'seaborn-v0_8'
    'dark_background'
    'fivethirtyeight'
    'classic'
    'bmh'

    See all available styles:
    print(plt.style.available)

## 15. Transparency
    plt.plot(x, y, alpha=0.7)

## 16. Save Figures
    plt.savefig('plot.png')

    Higher quality:
    plt.savefig('plot.png', dpi=300)
    
    Transparent background:
    plt.savefig('plot.png', transparent=True)

## 17. Full Example
    from matplotlib import pyplot as plt

    years = [2018, 2019, 2020, 2021, 2022]
    revenue = [5, 7, 9, 11, 14]

    plt.figure(figsize=(10, 5))

    plt.plot(
        years,
        revenue,
        color='green',
        linestyle='--',
        linewidth=3,
        marker='o',
        markersize=8,
        label='Revenue'
    )

    plt.title('Company Revenue Growth', fontsize=18)
    plt.xlabel('Year')
    plt.ylabel('Revenue in Millions')

    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.savefig('im/revenue_growth.png', dpi=300)
    plt.show()

## 18. Beginner Recommendations
    Good Beginner Style:
    plt.style.use('ggplot')

    Use:
    readable titles
    legends
    grids
    consistent colors
    figure sizes

## 19. Common Beginner Mistakes
    Forgetting plt.show():
    plt.show()

    Saving after show():
    Correct:
    plt.savefig('plot.png')
    plt.show()
    
    Too many colors => Keep plots simple and readable.

## 20. Recommended Learning Progression
    - Basic line plots
    - Titles and labels
    - Colors and markers
    - Multiple lines
    - Figure styles
    - Grids and legends
    - Bar charts
    - Scatter plots
    - Histograms
    - Subplots and advanced layouts