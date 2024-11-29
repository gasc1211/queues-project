"use client";
import { useForm } from "react-hook-form";
import z from "zod";
import { zodResolver } from "@hookform/resolvers/zod";

import { Input } from "@/components/ui/input";
import {
  Form,
  FormField,
  FormItem,
  FormDescription,
  FormLabel,
} from "@/components/ui/form";
import { Card } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const UserLoginSchema = z.object({
  email: z.string(),
  password: z.string()
})

export default function Login() {

  const form = useForm<z.infer<typeof UserLoginSchema>>({
    resolver: zodResolver(UserLoginSchema),
    defaultValues: {
      email: "",
      password: ""
    }
  });

  return (
    <main className="h-dvh flex items-center justify-evenly">
      <Card className="[&>*]:mt-4 w-1/3 px-8 py-4">
        <h2 className="font-bold text-center text-2xl">Queues Project</h2>
        <Form {...form}>
          <FormField control={form.control} name="email" render={({ field }) => (
            <FormItem>
              <FormLabel>Email</FormLabel>
              <Input placeholder="user@example.com" type="email" {...field} />
              <FormDescription>Enter your account email</FormDescription>
            </FormItem>
          )}
          />
          <FormField control={form.control} name="password" render={({ field }) => (
            <FormItem>
              <FormLabel>Password</FormLabel>
              <Input placeholder="********" type="password" {...field} />
              <FormDescription>Enter your account password</FormDescription>
            </FormItem>
          )}
          />
          <Button type="submit">Login</Button>
        </Form>
      </Card>
    </main>
  );
}