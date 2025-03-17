def app():
    import calendar
    num1 = int(input("Enter the Year:"))
    print(calendar.calendar(num1))
    app()
app()