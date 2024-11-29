"use client";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { FormDescription, FormLabel } from "@/components/ui/form";
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from "@/components/ui/input-otp"
import { useState } from "react";

export default function VerifyAccount() {

  const [value, setValue] = useState("")

  return (
    <main className="h-dvh flex items-center justify-around">
      <Card className="p-8">
        <form className="[&>*]:mt-4 flex flex-col align-middle">
          <h2 className="text-center font-bold">Verification Code</h2>
          <p className="text-sm font-light">Enter the verification code sent to your email address</p>
          <div className="mb-4 flex align-middle justify-center">
            <InputOTP
              maxLength={6}
              value={value}
              onChange={(value) => setValue(value)}
            >
              <InputOTPGroup>
                <InputOTPSlot index={0} />
                <InputOTPSlot index={1} />
                <InputOTPSlot index={2} />
                <InputOTPSlot index={3} />
                <InputOTPSlot index={4} />
                <InputOTPSlot index={5} />
              </InputOTPGroup>
            </InputOTP>
          </div>
          <Button type="submit">Verify Account</Button>
        </form>
      </Card>
    </main>
  );
}