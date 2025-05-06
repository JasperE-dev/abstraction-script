import syscalls as sys

axiom <T:size>type dynArray
   length:u64
   prv capacity:u64
   prv kind:T
   data:void*
   fn __init(self){}
   fn __del(self){}

axiom <T:size>type array
   cont length:u64
   prv kind:T
   data:void*
   fn __init(self){}
   fn __del(self){}

axiom type utf-8:
    data:u8[]
    pub fn len(self:str)u64{
       #todo redo so len give amount of chrs not len of memory 
       return self.data.len
    }

opt +(left:impl number, richt:impl number)impl number{
   fasm'
   add rax,rbx
   ret'
}

opt +(left:str, richt:str)str{
   newstr:str=left
   newstr.len+=richt.len
   newstr.data.append(richt.data)
   return newstr
}

fn print(msg:str){
	sys.STDOUT.write(msg+'\n',msg.len+1)
	ret
}

print('Hello, World!')
#print('Hello', 'world')
#print('q',1)

sys.exit(0)



