enum sysnum{
    read:64=0
    write
    open
    close

}

pub syscall(num:sysnum)64{
	fasm'syscall'
	ret
}


pub syscall(num:sysnum, arg0:64)64{
	fasm'
	push rdi
	mov rdi,rbx
	syscall
	pop rdi
	'
	ret
}


pub syscall(num:sysnum, arg0:64, arg1:64)64{
	fasm'
	push rsi
	push rdi
	mov rdi,rbx
	mov rsi,rcx
	syscall
	pop rdi
	pop rsi
	'
	ret
}


pub syscall(num:sysnum, arg0:64, arg1:64, arg2:64)64{
	fasm'
	push rsi
	push rdi
	mov rdi,rbx
	mov rsi,rcx
	syscall
	pop rdi
	pop rsi
	'
	ret
}

pub syscall(num:sysnum, arg0:64, arg1:64, arg2:64, arg3:64)64{
	fasm'
	push r10
	push rdi
	mov rdi, rbx
	mov r10, rsi
	mov rsi, rcx
	syscall
	pop rdi
	pop r10
	'
	ret
}


pub syscall(num:sysnum, arg0:64, arg1:64, arg2:64, arg3:64, arg4:64)64{
	fasm'
	push r8
	push r10
	mov r8,  rdi
	mov rdi, rbx
	mov r10, rsi
	mov rsi, rcx
	syscall
	pop r10
	pop r8
	'
	ret
}

pub syscall(num:sysnum, arg0:64, arg1:64, arg2:64, arg3:64, arg4:64, arg5:64)64{
	fasm'
	push r9
	push r10
	mov r9,  r8
	mov r8,  rdi
	mov rdi, rbx
	mov r10, rsi
	mov rsi, rcx
	syscall
	pop r10
	pop r9
	'
	ret
}

fn exit(code:8)noReturen:
    syscall(syscallnum.exit, code)

"""file descriptor""" # doc string
prv type FD{ # type name alwase start whit caphitel lether?
    self:64
    pub fn write(file:fd, buffer:u8[], size:u64):
	syscall(sysnums.write, file, bufer, size)
	ret
    
}



const STDIN=FD(0)
const STDOUT=FD(1)
const STDERR=FD(2)

