def count_ways_to_paint_fence(posts, colors):
    if posts == 0:
        return 0
    if posts == 1:
        return colors
    if posts == 2:
        return colors * colors

    # different_color[i]: ways to paint i posts where the last two have different colors
    different_color = [0] * (posts + 1)
    # same_color[i]: ways to paint i posts where the last two have same colors
    same_color = [0] * (posts + 1)
    # three_same_color[i]: ways to paint i posts where last three have the same color
    three_same_color = [0] * (posts + 1)

    # Base cases
    different_color[1] = colors
    same_color[1] = 0
    three_same_color[1] = 0

    different_color[2] = colors * (colors - 1)
    same_color[2] = colors
    three_same_color[2] = 0

    for i in range(3, posts + 1):
        different_color[i] = (different_color[i - 1] + same_color[i - 1] + three_same_color[i - 1]) * (colors - 1)
        same_color[i] = different_color[i - 1]
        three_same_color[i] = same_color[i - 1]

    total_ways = different_color[posts] + same_color[posts] + three_same_color[posts]
    return total_ways


if __name__ == "__main__":
    n = int(input("Enter number of posts: "))
    k = int(input("Enter number of colors: "))
    result = count_ways_to_paint_fence(n, k)
    print(f"Number of ways to paint the fence with {n} posts and {k} colors: {result}")
