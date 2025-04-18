emcc cubiomes/*.c -sEXPORTED_FUNCTIONS=_fill_area -sEXPORTED_RUNTIME_METHODS=ccall,cwrap
mv a.out.js static/
mv a.out.wasm static/
