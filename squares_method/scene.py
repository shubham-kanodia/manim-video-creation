from manim import *


class OptimisedPowerCalculation(Scene):
    def exit_elements(self, elements):
        self.play(*[FadeOut(element) for element in elements])

    def construct(self):
        # Part 1
        problem_statement = Text("Fast Exponentiation", font_size=80, color=ORANGE)
        description = Text(
            """
            In this video we will see how we can use squares method \n
            to do fast exponentiation
            """,
            font="Arial", font_size=32,
            slant=ITALIC,
            line_spacing=0.2,
            # t2c is a dict that you can choose color for different text
            t2c={"squares": ORANGE}
        )

        VGroup(problem_statement, description).arrange(DOWN, buff=1)
        self.play(Write(problem_statement))
        self.wait(1)
        self.play(FadeIn(description))

        self.wait(3)
        self.exit_elements([problem_statement, description])

        # End of part 1

        # Part 2
        solution_part_1_top_text = Tex(
            """
            We will define a function that takes in g and x as inputs \n
            and calculates $g^x$
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
            $""", font_size=40, color=ORANGE
        )

        VGroup(solution_part_1_top_text, solution_part_1).arrange(DOWN, buff=MED_LARGE_BUFF)
        self.play(FadeIn(solution_part_1_top_text), Write(solution_part_1))

        self.wait(23)
        self.exit_elements([solution_part_1_top_text, solution_part_1])

        # End of part 2

        # Part 3
        play_kw = {"run_time": 4}

        solution_part_2_top_text = Tex(
            """
            Let's take an example of $2^15$ to break this down \n\n
            """, font_size=50
        )
        solution_part_2_bottom_text = Text(
            """
            Here g is 2 and x is 15
            """,
            font_size=30,
            slant=ITALIC,
            t2c={"Here g is 2 and x is 15": ORANGE}
        )
        VGroup(solution_part_2_top_text, solution_part_2_bottom_text).arrange(DOWN, buff=MED_LARGE_BUFF)

        self.play(Write(solution_part_2_top_text))
        self.wait(1)
        self.play(Write(solution_part_2_bottom_text))
        self.wait(3)
        self.play(FadeOut(solution_part_2_top_text), FadeOut(solution_part_2_bottom_text))

        # End of part 3

        solution_list = VGroup(
            Tex(r"$2^15 = f(2, 15)$"),
            Tex(r"$\therefore 2^15 = 2 * f(2^2, \dfrac{(15 - 1)}{2} = 2 * f(4, 7)$"),
            Tex(r"$\therefore 2^15 = 2 * [4 * f(4^2, \dfrac{7 - 1}{2})] = 2 * 4 * f(16, 3)$"),
            Tex(r"$\therefore 2^15 = 2 * 4 * [16 * f(16^2, \dfrac{3 - 1}{2})] = 2 * 4 * 16 * f(256, 1)$"),
            Tex(r"$\therefore 2^15 = 2 * 4 * 16 * 256$"),
            Tex(r"$\therefore 2^15 = 32786$")
        )
        solution_list.arrange(DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)

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

        self.play(
            TransformMatchingTex(
                solution_list[4].copy(), solution_list[5],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )

        self.wait(10)
