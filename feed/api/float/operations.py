
import numpy as np

from feed.core.base import Stream

from feed.core.operators import BinOp

from feed.api.float import Float


@Float.register(["add", "__add__"])
def add(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    if np.isscalar(s2):
        s2 = Stream.constant(s2, dtype="float")
        return BinOp(np.add)(s1, s2).astype("float")
    return BinOp(np.add)(s1, s2).astype("float")


@Float.register(["radd", "__radd__"])
def radd(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    return add(s1, s2)


@Float.register(["sub", "__sub__"])
def sub(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    if np.isscalar(s2):
        s2 = Stream.constant(s2, dtype="float")
        return BinOp(np.subtract)(s1, s2).astype("float")
    return BinOp(np.subtract)(s1, s2).astype("float")


@Float.register(["rsub", "__rsub__"])
def rsub(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    if not np.isscalar(s2):
        raise Exception("Invalid node operation.")
    s2 = Stream.constant(s2, dtype="float")
    return BinOp(np.subtract)(s2, s1).astype("float")


@Float.register(["mul", "__mul__"])
def mul(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    if np.isscalar(s2):
        s2 = Stream.constant(s2, dtype="float")
        return BinOp(np.multiply)(s1, s2).astype("float")
    return BinOp(np.multiply)(s1, s2).astype("float")


@Float.register(["rmul", "__rmul__"])
def rmul(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    return mul(s1, s2)


@Float.register(["div", "__truediv__"])
def truediv(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    if np.isscalar(s2):
        s2 = Stream.constant(s2, dtype="float")
        return BinOp(np.divide)(s1, s2).astype("float")
    return BinOp(np.divide)(s1, s2).astype("float")


@Float.register(["rdiv", "__rtruediv__"])
def rtruediv(s1: "Stream[float]", s2: "Stream[float]") -> "Stream[float]":
    if not np.isscalar(s2):
        raise Exception("Invalid node operation.")
    s2 = Stream.constant(s2, dtype="float")
    return BinOp(np.divide)(s2, s1).astype("float")


@Float.register(["abs", "__abs__"])
def abs(s: "Stream[float]") -> "Stream[float]":
    return s.apply(np.abs).astype("float")


@Float.register(["neg", "__neg__"])
def neg(s: "Stream[float]") -> "Stream[float]":
    return s.apply(np.negative).astype("float")


@Float.register(["pow", "__pow__"])
def pow(s: "Stream[float]", power: float) -> "Stream[float]":
    return s.apply(lambda x: np.power(x, power)).astype("float")