#load assemblys for listening to keys
Add-Type -AssemblyName WindowsBase
Add-Type -AssemblyName PresentationCore
function New-DeliverooCounter {
    #init count and 'gui'
    [console]::BackgroundColor = 'White'
    Clear-Host
    $count = 0
    Write-Host "Meals Since Deliveroo!!!" -ForegroundColor 'White' -BackgroundColor 'DarkRed'
    Write-Host "`n`n            $count" -ForegroundColor Red

    while ($true){
        #listen for keys n or d
        $isDeliveroo = [Windows.Input.Keyboard]::IsKeyDown([System.Windows.Input.Key]::d)
        $notDeliveroo = [Windows.Input.Keyboard]::IsKeyDown([System.Windows.Input.Key]::n)
        #if D is pressed, reset count to 0, then display the output
        if ($isDeliveroo) {
            Clear-Host
            $count = 0
            Write-Host "Meals Since Deliveroo!!!" -ForegroundColor 'White' -BackgroundColor 'DarkRed'
            Write-Host "`n`n            $count" -ForegroundColor Red
            #reset variable to false
            $isDeliveroo = $false
        }
        #if N is pressed, increment 1, then display the output
        elseif ($notDeliveroo) {
            Clear-Host
            $count++
            Write-Host "Meals Since Deliveroo!!!" -ForegroundColor 'White' -BackgroundColor 'DarkRed'
        #display output in colour dependant on number
            if($count -ge 6) {
                Write-Host "`n`n            $count" -ForegroundColor Green
            }
            elseif($count -ge 4) {
                Write-Host "`n`n            $count" -ForegroundColor DarkYellow
            }
            elseif($count -le 3) {
                Write-Host "`n`n            $count" -ForegroundColor Red
            }
            #reset variable to false
            $notDeliveroo = $false
        }
        Start-Sleep -Seconds 1
    }
}






