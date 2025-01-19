from sys import argv as args

if len(args)!=2:
    print('error: cmd file')
    exit(1)

fd=open(args[1])
input=fd.read()

print(input)





"""
i give up ):
odin run src/main.odin -file -- src/q.as
main.odin:
package main

import "core:fmt"
import "core:os"
import "core:strings"

read_file_by_lines_in_whole :: proc(filepath: string)-> string {
	data, ok := os.read_entire_file(filepath, context.allocator)
	if !ok {
        fmt.printfln("error: opening file")
        os.exit(1)
	}
	defer delete(data, context.allocator)

	it := string(data)
	return it
}


main :: proc() {
	fmt.println("args:",os.args)
    if len(os.args)!=2{
        fmt.printfln("error: expect cmd file")
        os.exit(1)
    }
    fmt.printfln(read_file_by_lines_in_whole(os.args[1]
    ))
}


/*   
    input:=[]byte{}
    length:int
    length,err=os.read(fd,input)
    if err != nil {
        fmt.printfln("error: reading file")
        os.exit(1)
    }
    fmt.printfln(string(input))
*/
"""