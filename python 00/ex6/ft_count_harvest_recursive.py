# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kle-scor <kle-scor@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 11:34:53 by kle-scor          #+#    #+#              #
#    Updated: 2026/03/25 11:34:55 by kle-scor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def helper(y, x):
    if y <= x:
        print("Day ", y)
        helper(y + 1, x)


def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    y = 1

    helper(y, x)
    print("Harvest time!")
