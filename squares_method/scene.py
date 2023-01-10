from manim import *


class OptimisedPowerCalculation(Scene):
    def exit_elements(self, elements):
        self.play(*[FadeOut(element) for element in elements])

    def construct(self):
        # Part 1
        problem_statement = Tex("Calculating ", "$g^x$", " using squares method", font_size=80)
        description = Text(
            """
            In this video we will see how we can use \"squares\" method \n
            to do fast exponentiation.
            """,
            font="Arial", font_size=32,
            # t2c is a dict that you can choose color for different text
            t2c={"squares": ORANGE}
        )

        VGroup(problem_statement, description).arrange(DOWN, buff=1)
        self.play(Write(problem_statement))
        self.wait(2)
        self.play(FadeIn(description))

        self.wait(1)
        self.exit_elements([problem_statement, description])

        # End of part 1

        # Part 2
        solution_part_1_top_text = Tex(
            """
            We will define a function that takes in g and x as inputs \n
            and calculates result in logarithmic time complexity
            """, font_size=40
        )

        solution_part_1 = Tex(
            r"""$
            f(g, x) =
                \left\{
                    \begin{array}{ll}
                        g * f(g^2, (x - 1)/2)  & \mbox{if } \mbox{x mod 2} \not= 0 \\
                        f(g^2, x/2) & \mbox{if } \mbox{x mod 2} = 0 \\
                        1 & \mbox{if } x = 0
                    \end{array}
                \right.
            $""", font_size=40
        )

        VGroup(solution_part_1_top_text, solution_part_1).arrange(DOWN, buff=1)
        self.play(Write(solution_part_1_top_text), FadeIn(solution_part_1))

        self.wait(3)
        self.exit_elements([solution_part_1_top_text, solution_part_1])

        # End of part 2

        # Part 3
        play_kw = {"run_time": 2}

        solution_part_2_top_text = Tex(
            """
            Let's take an example of $2^15$ to break this down \n\n
            Here g = 2 and x = 15
            """, font_size=40
        )

        self.play(Write(solution_part_2_top_text))
        self.wait(3)
        self.play(FadeOut(solution_part_2_top_text))

        # End of part 3

        solution_list = VGroup(
            Tex(r"$= 2 * f(2^2, \dfrac{(15 - 1)}{2} = 2 * f(4, 7)$"),
            Tex(r"$= 2 * [4 * f(4^2, \dfrac{7 - 1}{2}] = 2 * 4 * f(16, 3)$"),
            Tex(r"$= 2 * 4 * [16 * f(16^2, \dfrac{3 - 1}{2}] = 2 * 4 * 16 * f(256, 1)$"),
            Tex("$= 2 * 4 * 16 * 256$"),
            Tex("$= 32786$")
        )
        solution_list.arrange(DOWN, buff=MED_SMALL_BUFF)

        self.add(solution_list[0])
        self.play(
            TransformMatchingTex(
                solution_list[0].copy(), solution_list[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )

        self.play(
            TransformMatchingTex(
                solution_list[1].copy(), solution_list[2],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )

        self.play(
            TransformMatchingTex(
                solution_list[2].copy(), solution_list[3],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )

        self.play(
            TransformMatchingTex(
                solution_list[3].copy(), solution_list[4],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )

        self.wait(2)
