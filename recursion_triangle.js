function hash(x) {
    let s = "";
    for (i = 0; i < x; i++) {
        s += '#';
    }
    return s;
}
    

function recurse(n) {
    if (n === 0) {
        return 1;
    } else {
        recurse(n - 1);
        console.log(hash(n));
    }
}

recurse(7)


