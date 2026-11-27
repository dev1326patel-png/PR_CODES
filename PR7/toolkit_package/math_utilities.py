"""Mathematical utility functions used by the Multi-Utility Toolkit."""

import math


def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if not isinstance(number, int) or isinstance(number, bool) or number < 0:
        raise ValueError("Factorial requires a non-negative integer.")
    return math.factorial(number)


def compound_interest(principal: float, annual_rate: float, years: float,
                      compounds_per_year: int = 1) -> tuple[float, float]:
    """Return (final amount, compound interest earned). Rate is entered as a percent."""
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("Principal, rate, and time cannot be negative.")
    if compounds_per_year <= 0:
        raise ValueError("Compounds per year must be greater than zero.")
    amount = principal * (1 + annual_rate / (100 * compounds_per_year)) ** (
        compounds_per_year * years
    )
    return amount, amount - principal


def trigonometry(angle_degrees: float) -> dict[str, float]:
    """Return sine, cosine, and tangent for an angle in degrees."""
    radians = math.radians(angle_degrees)
    tangent = math.tan(radians)
    if math.isclose(math.cos(radians), 0.0, abs_tol=1e-12):
        tangent = float("inf")
    return {
        "sin": math.sin(radians),
        "cos": math.cos(radians),
        "tan": tangent,
    }


def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2


def rectangle_area(length: float, width: float) -> float:
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width


def triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height
