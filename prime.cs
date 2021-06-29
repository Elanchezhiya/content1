int num= Convert.ToInt32(Console.ReadLine());

            int ct = 0, n = 0, i = 1, j = 1;
            while (n < num)
            {
                j = 1;
                ct = 0;
                while (j <= i)
                {
                    if (i % j == 0)
                        ct++;
                    j++;
                }
                if (ct == 2)
                {
                    Console.Write(i);
                    Console.Write(" ");
                    n++;
                }
                i++;
            }
            Console.ReadLine();
